from flask import Flask, request, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, j0nixDB
from random import randrange
import logging

# Set logging stuff
logger = logging.getLogger("j0nixRulez")
logger.setLevel(logging.DEBUG)

# Connect to Database and create database session
engine = create_engine("sqlite:///j0nix-rulez.db?check_same_thread=False")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

""" Fetch all wisdoms """


def get_all_wisdom():
    try:
        wisdoms = session.query(j0nixDB).all()
    except Exception as e:
        logger.error("Failed fetching all wisdoms, error: {}".format(e))
        return jsonify({"error": "{}".format(e)})

    return jsonify(wisdoms=[b.serialize for b in wisdoms])


""" Fetch wisdom by id """


def get_wisdom(wisdom_id):
    try:
        wisdoms = session.query(j0nixDB).filter_by(id=wisdom_id).one()
    except Exception as e:
        logger.error("Failed fetching wisdom {}, error: {}".format(wisdom_id, e))
        return jsonify({"error": "{}".format(e)})

    return jsonify(wisdoms=wisdoms.serialize)


""" Add a new wisdom to the database """


def makeANewWisdom(msg):
    try:
        addedwisdom = j0nixDB(msg=msg)
        session.add(addedwisdom)
        session.commit()
    except Exception as e:
        logger.error("Failed to add wisdom, error: {}".format(e))
        return jsonify({"error": "{}".format(e)})

    return jsonify(j0nixDB=addedwisdom.serialize)


""" Update a wisdom in the database """


def updateAWisdom(id, msg):
    try:
        updatedWisdom = session.query(j0nixDB).filter_by(id=id).one()
        if msg:
            updatedWisdom.msg = msg
        session.add(updatedWisdom)
        session.commit()
    except Exception as e:
        logger.error("Failed to update wisdom {}, error: {}".format(id, e))
        return jsonify({"error": "{}".format(e)})

    return jsonify({"info": "Updated a j0nixDB widom with id {}".format(id)})


""" Remove a wisdom """


def deleteAWisdom(id):
    try:
        wisdomToDelete = session.query(j0nixDB).filter_by(id=id).one()
        session.delete(wisdomToDelete)
        session.commit()
    except Exception as e:
        logger.error("Failed to delete wisdom {}, error: {}".format(id, e))
        return jsonify({"error": "{}".format(e)})

    return jsonify({"info": "Removed j0nixDB wisdom with id {}".format(id)})


""" Get a random wisdom """


def randomizedWizdom():
    try:
        rows = session.query(func.count(j0nixDB.id)).scalar()
    except Exception as e:
        logger.error("Failed counting wisdoms in database, error: {}".format(e))
    else:
        if rows > 0:
            wisdom_id = randrange(1, rows + 1)
            try:
                wisdoms = session.query(j0nixDB).filter_by(id=wisdom_id).one()
            except Exception as e:
                logger.info("Trying another wisdom")
                return randomizedWizdom()

            return jsonify(wisdoms=wisdoms.serialize)

        return get_all_wisdom()


# All the routes
@app.route("/")
@app.route("/wisdoms", methods=["GET", "POST"])
def wisdomsFunction():
    """ Get all wisdoms (both in server root and under /wisdom) """
    if request.method == "GET":
        return get_all_wisdom()

    """ Add a new wisdoms (both in server root and under /wisdom)"""
    if request.method == "POST":
        msg = request.args.get("msg", "")
        return makeANewWisdom(msg)


@app.route("/wisdoms/<int:id>", methods=["GET", "PUT", "DELETE"])
def wisdomsByIdFunction(id):
    """ Get a wisdom by id"""
    if request.method == "GET":
        return get_wisdom(id)

    """ Update a wisdom by id """
    if request.method == "PUT":
        msg = request.args.get("msg", "")
        return updateAWisdom(id, msg)

    """ Delete a wisdom by id """
    if request.method == "DELETE":
        return deleteAWisdom(id)


@app.route("/random", methods=["GET"])
def randomWisdomFunction():
    """ Go get a random wisdom """
    return randomizedWizdom()


if __name__ == "__main__":
    """ Using built in server..."""
    app.debug = True
    app.run(host="0.0.0.0", port=8080)

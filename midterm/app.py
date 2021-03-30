from flask import Flask, request, abort
import json
import database

app = Flask(__name__)


@app.route('/animals', methods = ['GET'])
def animals():
    num_of_animals = request.args.get('num_of_animals')

    if num_of_animals is None:
        num_of_animals = 100

    try:
        num_of_animals = int(num_of_animals)
    except:
        abort(400, "'num_of_animals' must be of type int.")

    database.sum_animals(num_of_animals)

    return "Code Runs"

  
  
@app.route('/clear', methods = ['GET'])
def clear():
    try:
        database.delete_animals()
    except:
        abort(500)

    return "The code ran"


# query a range of dates                                                                                                                                                                                                                                                                                                                                
@app.route('/get_animals_by_dates')
def query_dates():
    beginning_date = request.args.get('beginning_date')
    end_date = request.args.get('end_date')

    try:
        assert beginning_date is not None
        assert end_date is not None
    except AssertionError:
        abort(400)

    try:
        return json.dumps( database.query_dates(beginning_date, end_date), indent=2 )
    except AssertionError:
        abort(400)
    except:
        abort(500)





#Selecting  a particular creature through UUID                                                                                                                                                                                                                                                                                                          
@app.route('/get_creature_by_uuid')
def get_creature_by_uuid():
    unique = request.args.get('uuid')

    try:
        assert unique is not None
    except AssertionError:
        abort(400)

    try:
        return databases.get_creature_by_uuid(unique)
    except:
        abort(404)


#edits a creature through UUID                                                                                                                                                                                                                                                                                                                          
@app.route('/edit_creature_by_uuid', methods=['POST'])
def edit_creature_by_uuid():
    unique = request.args.get('uuid')

    try:
        assert unique is not None
        new_traits = request.get_json()
    except AssertionError:
        abort(400, "\'unique\' must be provided!")
    except:
        abort(400)

    database.edit_creature_by_uuid(unique, new_traits)

    return "Success!\n"

  
  
#Deletes a selection of animals by a date randees                                                                                                                                                                                                                                                                                                       
@app.route('/delete_through_dates', methods=['GET'])
def delete_by_dates():
    beginning_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        assert beginning_date is not None
        assert end_date is not None
    except AssertionError:
        abort(400)

    try:
        database.delete_date_range(beginning_date, end_date)
        return "Success!\n"
    except AssertionError:
        abort(400)
    except:
        abort(500)

        

#returns the avaerage of legs                                                                                                                                                                                                                                                                                                                           
@app.route('/get_average_legs', methods=['GET'])
def get_average_num_of_legs():
    try:
        return str( database.get_average_num_of_legs() ) + '\n'
    except:
        abort(500)


#returns the total count                                                                                                                                                                                                                                                                                                                                
@app.route('/total_count', methods=['GET'])
def total_count():
    try:
        return str( database.total_count() ) + '\n'
    except:
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

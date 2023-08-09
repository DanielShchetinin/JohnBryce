from flask import Flask, request, jsonify
import psycopg2
import datetime

app = Flask("Bank_Web_Api")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")


@app.route('/')
def main():
    query = """
    <h1>Welcome<h1>
    
    <h3>To get information about customer:
    /api/v1/customers/customer_id<h3>
    
    <h3>To get information about accounts of customer: /api/v1/customers/customer_id/accounts<h3>
    
    <h3>To change information about customer: /api/v1/customers/customer_id with PUT<h3>
    
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    
    """
    return query


@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def customers(customer_id):
    print(f"Called to: /api/v1/customers/customer_id/{customer_id}")
    try:
        with conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM customers WHERE id = %s"
                cur.execute(sql, (customer_id,))
                result = cur.fetchone()
                print(f"Result from fetchone: {result}")
                if result:
                    ret_data = {
                        'id': result[0],
                        'passport number': result[1],
                        'name': result[2],
                        'address': result[3]
                    }
                    return jsonify(ret_data)
                else:
                    return {"error": f'customer with id {customer_id} does not exist'}, 404

    except psycopg2.DatabaseError as error:
        return {'error': f"Database Error"}, 500
    except Exception as error:
        return {'error': f"Unexpected Error"}, 500


@app.route("/api/v1/customers/<int:customer_id>/accounts", methods=['GET'])
def customers_accounts(customer_id):
    print(f"Called to: /api/v1/customers/customer_id/{customer_id}/accounts")
    try:
        with conn:
            with conn.cursor() as cur:
                sql = """
                SELECT customers."name", accounts.* from customers
                join account_owners on customers.id = account_owners.customer_id
                join accounts on accounts.id = account_owners.account_id
                where customers.id = %s
                """
                cur.execute(sql, (customer_id,))
                result_list = []
                result = cur.fetchall()
                for i in result:
                    if len(result) == 0:
                        print("Broken")
                        break
                    if i:
                        ret_data = {
                            'name': i[0],
                            'account id': i[1],
                            'balance': i[2],
                            'limits': i[3],
                        }
                        result_list.append(ret_data)
                    else:
                        return {"error": f'customer with id {customer_id} does not exist'}, 404
                if len(result) == 0:
                    return {"error": f'customer with id {customer_id} does not exist'}, 404
                print(f"Sending result: \n{result_list}")
                return jsonify(result_list)

    except psycopg2.DatabaseError as error:
        print(error)
        return {'error': f"Database Error"}, 500
    except Exception as error:
        print(error)
        return {'error': f"Unexpected Error"}, 500

@app.route("/api/v1/customers/<int:customer_id>", methods=['PUT'])
def customers_update(customer_id):
    print(f"Called to: /api/v1/customers/customer_id/{customer_id} | with PUT")
    new_data = request.form
    updates_str_list = []
    allowed_fields = ('name', 'address')
    for field in new_data:
        if field in allowed_fields:
            updates_str_list.append(f"{field}=%s")
    sql = f"UPDATE customers SET {','.join(updates_str_list)} WHERE id=%s"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.values()) + (customer_id,))
            if cur.rowcount == 1:
                return app.response_class(status=200)
    return app.response_class(status=500)

@app.route("/api/v1/customers", methods=['POST'])
def create_customers():
    print(f"Called to: /api/v1/customers/ | with POST")
    required_fields = {
        'passport_num': int,
        'name': str,
        'address': str,
    }
    if set(request.form.keys()) != set(required_fields.keys()):
        return {'error': 'error in provided fields'}, 400

    str_list = []
    for field in request.form:
        try:
            required_fields[field](request.form[field])
            str_list.append(field)
        except:
            return {'error': f'invalid type for {field}, '
                    f'expected: {required_fields[field]}, got {type(field)}'}, 400
    sql = f"INSERT INTO customers ({','.join(request.form.keys())}) VALUES ({','.join(['%s'] * 3)})"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(request.form.values()))
            if cur.rowcount == 1:
                return {}, 200
    return {}, 500



if __name__ == '__main__':
    start = datetime.datetime.now()
    app.run(host='0.0.0.0', port=4747, debug=True)
    end = datetime.datetime.now()
    date = end.strftime("%d.%m.%Y")
    time = end.strftime("%H:%M")
    run_time = (end - start).total_seconds()
    print("\n"*25)
    print("\nProgram Run Time:", run_time, "Seconds\n")
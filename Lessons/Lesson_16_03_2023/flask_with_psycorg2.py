from flask import Flask, request, jsonify
import psycopg2

app = Flask("Bank_Web_Api")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")


@app.route('/')
def main():
    return "<h1>Welcome<h1>"

@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def customers(customer_id):
    print(f"Called to: /customers/customer_id/{customer_id}")
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


'@app.route("/api/v1/customers/<int:customer_id>/accounts", methods=['GET'])
def customers(customer_id):
    print(f"Called to: /customers/customer_id/{customer_id}/accounts")
    try:
        with conn:
            with conn.cursor() as cur:
                sql = """
                select c.id, c."name", a.id, a.balance from customers c
                join account_owners ao on c.id = ao.customer_id
                join accounts a on a.id = ao.account_id
                where c.id = %s
                """'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4747, debug=True)





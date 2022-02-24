import psycopg2

def main():
    print('init')
    bucket = 'my_bucket'
    key = 'path/filename.json'
    record_path = './new2.json'


    conn_str = 'postgres://postgres:docker@localhost:5432'
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()

    f = open(record_path, "r")


    cur.copy_expert('COPY json_table (data) FROM STDIN;', f)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()  
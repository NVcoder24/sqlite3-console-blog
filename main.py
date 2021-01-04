import sqlite3
import os

os_type = os.name

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def clean():
    if os_type == "nt":
        os.system("cls")
    elif os_type == "unix":
        os.system("clear")
    else:
        print("unexpected error!")

def read(id=""):
    sql = f"""
    SELECT * FROM posts WHERE id=?;
    """
    cursor.execute(sql, id)
    return cursor.fetchall()
    conn.commit()

def write(array=[]):
    sql=f"""
    INSERT INTO posts VALUES (?,?,?);
    """
    cursor.execute(sql, [array[0],array[1],array[2]])
    conn.commit()

def delete(id=""):
    sql=f"""
    DELETE FROM posts WHERE id=?;
    """
    cursor.execute(sql, id)
    conn.commit()

def display_post(array=[]):
    print(f"we received:{array}")
    print(f"\n{array[0]}\n{array[1]}\n")

while(0<1):
    a = input("what do you want to do? (0 - read post, 1 - write post, 2 - delete post, 3 - exit, 4 - clean terminal): ")
    if a == "0":
        b = input("please enter id of post you need: ")
        resp = read(b)
        if resp == []:
            print("wrong id!")
        else:
            display_post([resp[0][0],resp[0][1]])
    elif a == "1":
        t = input("title of the post: ")
        txt = input("text  of the post: ")
        id = input("id    of the post: ")
        write([t,txt,id])
        print("success!")
    elif a == "2":
        id = input("id of the post to delete: ")
        while(True):
            yn = input("ARE YOU SURE ABOUT THAT (yes or no): ")
            if yn == "yes":
                yn = True
                break
            elif yn == "no":
                yn = False
                break
            else:
                print("please try again!")
        if yn == True:
            print(f"post deleted: id {id}")
            delete(id)
        else:
            print("canceled")
    elif a == "3":
        print("good bye!")
        break
    elif a == "4":
        clean()
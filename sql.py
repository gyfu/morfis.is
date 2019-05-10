#Höfundur: Huginn Þór Jóhannsson
import sqlite3
adgangar=sqlite3.connect("adgangar.db")
domarar=sqlite3.connect("domarar.db")
ca=adgangar.cursor()
cd=domarar.cursor()
#Búa til aðganga
ca.execute('''CREATE TABLE if not exists users(
        user varchar(32) NOT NULL,
        pass varchar(32) NOT NULL
        );
        '''
        )
ca.execute('''INSERT or ignore INTO users(
        user,
        pass
        )
        VALUES
        (
        "admin",
        "password"
        );
        '''
        )
ca.execute('''SELECT * FROM users''')
print(ca.fetchone())
adgangar.commit()
adgangar.close()
cd.execute('''CREATE TABLE if not exists domarar(
        nafn varchar(32) NOT NULL,
        model varchar(32),
        skoli varchar(32) NOT NULL,
        simi varchar(32)
        );
        '''
        )
cd.execute('''INSERT or ignore INTO domarar(
        nafn,
        model,
        skoli,
        simi
        )
        VALUES
        (
        "Huginn Þór Jóhannsson",
        "2000",
        "Tækniskólinn",
        "8579950"
        );
        '''
        )
print(cd.fetchone())
domarar.commit()
domarar.close()

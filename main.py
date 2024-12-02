import threading
import json
import program_1,program_2,program_3

def main():
    with open("configs//config.json",'r') as config_json:
        config = json.loads(config_json.read())
        print(config["programs"]["file_name"]["program_1.py"]["Input"])
        print(config["programs"]["file_name"]["program_2.py"]["Input"])
        print(config["programs"]["file_name"]["program_3.py"]["Input"])
    
    t1 = threading.Thread(target=program_1.main())
    t2 = threading.Thread(target=program_2.main())
    t3 = threading.Thread(target=program_3.main())
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main()

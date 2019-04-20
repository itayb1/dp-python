from apiwrapper import dpAPI


def main():
    api = dpAPI.DpAPI("https://0.0.0.0:5554/", ("admin", "admin"), "default")
    allowed_methods = ("get", "delete", "put", "post", "head")
    #print(api.handler.create_http_handler("Testsfp", "0.0.0.0", 7058, "enabled", allowed_features=allowed_methods, MaxValueHdrLen=50))
    

    # create rule
    #api.match_action.create()
    mpgw_name = "BestMPGW5"
    get_queue = "Best_MQ_2"
    


    # api.mq_handler.create(name=get_queue + "_F13", queue_manager="Test_mq_mangaer_grp", get_queue=get_queue, state="enabled")
    handler = api.mq_handler.get("Best_MQ_2_F13")
    api.mq_handler.update(handler, ParseProperties="off", mAdminState="disabled")
    


if __name__ == "__main__":
    main()
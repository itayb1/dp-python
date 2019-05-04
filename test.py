from dpAPI import dpAPI


def main():
    api = dpAPI.DpAPI("https://0.0.0.0:5554/", ("admin", "admin"), "default")
    allowed_methods = ("get", "delete", "put", "post", "head")
    #print(api.handler.create_http_handler("Testsfp", "0.0.0.0", 7058, "enabled", allowed_features=allowed_methods, MaxValueHdrLen=50))


    # create rule
    #api.match_action.create()
    mpgw_name = "BestMPGW5"
    get_queue = "Best_MQ_2"

    #http_handler = api.http_handler.create("test_http_fsh", "0.0.0.0", 4512, "enabled", ["get", "post", "options"])

    # api.mq_handler.create(name=get_queue + "_F13", queue_manager="Test_mq_mangaer_grp", get_queue=get_queue, state="enabled")

    try:
        handler = api.mq_handler.delete("test_mq_FSH4")
        print(handler)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()

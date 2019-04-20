from apiwrapper import dpAPI
import sys

test = dpAPI.DpAPI("https://0.0.0.0:5554", ("admin", "admin"), "default")
test.mpgw.create


if __name__ == "__main__":
    # Usage - python3 create_mpgw.py DP_REST_API HANDLERS_LIST
    print(sys.argv[1])
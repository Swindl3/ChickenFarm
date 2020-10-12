import requests
import json


class ChickenFarm:
    def __init__(self):
        self.dhtNetPieKey = {
            "dhtKeyOne": ["b7f3088b-479a-469d-b48f-dbe1724f15e5", "sJ6zDf4YfxYN82iWtgqWvFNPCNu4Af1B"],
            "dhtKeyTwo": ["25140ab3-44ed-49b6-879b-8ef99cd1d304", "5ZMCyEKyfRfd37pY5CazbhF3TbgxSUgW"],
            "dhtKeyThree": ["2ea97004-8ad3-49e7-96b6-35aec0e99261", "Z7q4NAiWCdMpya56VSgNiDrZaMhp78sz"],
            "dhtKeyFour": ["cb6f6d1e-6d94-43d5-ba1b-c0797454be29", "HjfSWBqUNsHVFtwA718y42owkL2wrEaC"],
            "dhtKeyFive": ["7ca9a74b-d425-4506-9809-9db61756d17c", "v86YiCwUj2fwxriEBZLR6nQz2sAhN96N"],
            "dhtKeySix": ["f8e5895c-e630-4f40-8f04-f3c32dbeed1f", "zuBmacuhRnE2gJYSz4x4qVzZNg1NX84t"],
            "dhtKeySeven": ["f5e8ba5f-b816-4391-9d61-6aa16157ed44", "m356ZZXhuTpDaHzJXt2yCaRpz8oFz6kP"],
            "dhtKeyEight": ["30833898-10db-4aed-9824-6a3ff4617f19", "UioXAMDdbSGQTAbnS8hb7LJKEtgu2XY4"],
            "dhtKeyNine": ["722e3a47-ba79-4150-a8c0-616757497217", "kmMdsXdr6XzyX6pGuzV5VnkQYuEy8q5Q"]
        }
        self.fanSpeedNetPieKey = {
            "fanKeyOne": ["6919ce4d-bf5c-478c-836a-06ca66b147ee", "gnpeSQUzNFbtWjCjBqHxno2oTRrQDsUV"],
            "fanKeyTwo": ["cf059303-48e4-48cb-9b0b-ae41e012c3b0", "cnzpyyca2NHdTDiQCxytn9j6fuwvszDZ"],
            "fanKeyThree": ["929f3b8e-bf9e-4367-b214-3028f29036cc", "S5jVzCfW1JVaAUsH3ct92yQ2uUUG4LgC"],
        }

    def getMeanTempHumiVal(self):
        tempVal = []
        humidVal = []
        count = 0
        for key in self.dhtNetPieKey.values():
            count += 1
            print(count)
            r = requests.get('https://api.netpie.io/v2/device/shadow/data',
                             auth=(key[0], key[1]))
            jsonData = json.loads(r.text)
            tempVal.append(int(jsonData["data"]["temperature"]))
            humidVal.append(int(jsonData["data"]["humidity"]))
            print(jsonData["data"])
            print(type(jsonData))
        print("All temp val : ", len(tempVal))
        print("All humid val : ", len(humidVal))
        meanTempVal = round(sum(tempVal) / len(tempVal), 2)
        meanHumidVal = round(sum(humidVal) / len(humidVal), 2)

        print("meanTempVal", meanTempVal)
        print("meanHumidVal", meanHumidVal)
        print("List of tempVal", tempVal)
        print("List of humidVal", humidVal)
        return [meanTempVal, meanHumidVal]

    def getMeanFanSpeedVal(self):
        fanSpeedVal = []
        for key in self.fanSpeedNetPieKey.values():
            r = requests.get('https://api.netpie.io/v2/device/shadow/data',
                             auth=(key[0], key[1]))
            jsonData = json.loads(r.text)
            fanSpeedVal.append(float(jsonData["data"]["Wind"]))
            print(jsonData["data"]["Wind"])
        meanSpeedVal = sum(fanSpeedVal) / len(fanSpeedVal)
        print("List fanSpeedVal : ", fanSpeedVal)
        return meanSpeedVal


def main():
    chicken = ChickenFarm()
    meanTemp, meanHumid = chicken.getMeanTempHumiVal()
    meanSpeedFan = chicken.getMeanFanSpeedVal()
    print("Average temperature : ", meanTemp)
    print("Average humidity : ", meanHumid)
    print("Average speed fans : ", meanSpeedFan)


if (__name__ == "__main__"):
    main()

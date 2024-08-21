import os
import hashlib


def hashCompute(data: str):
    hashFunc = hashlib.md5()
    hashFunc.update(data.encode("UTF-8"))
    return hashFunc.hexdigest()


def serializeBinData(filename: str, data: any):
    with open(filename, "wb") as wf:
        serializedBinDataList = []
        for dat in data:
            serializedBinDataList.append(" ".join(str(bin(ord(da))) for da in dat))
            serializedBinDataList.append("|")
        if serializedBinDataList:
            print("[*] Binary Serialization complete!")
            serializedDataStream = "".join(data for data in serializedBinDataList)
            checksum = hashCompute(serializedDataStream)
        else:
            print("[-] Binary Serialization failed!!")
        for data in serializedBinDataList:
            wf.write(data.encode("UTF-8"))
        checksumBin = " ".join(str(bin(ord(char))) for char in checksum)
        wf.write(checksumBin.encode("UTF-8"))
        print("[*] Binary data written successfully!")


def deserializeBinData(filename: str):
    if not os.path.exists(filename):
        print("[-] Binary File doesnt exist")
        return -1
    with open(filename, "rb") as rf:
        data = rf.read().decode("UTF-8")
        data_stream, checksum = data.rsplit("|", 1)
        realChecksum = "".join(chr(int(char, 2)) for char in checksum.split(" "))
        data_stream = data_stream.split("|")
        print("[+] Binary file decoded!")
        deserializedBinData = []
        deserializedChecksumBin = []
        for line in data_stream:
            chars = line.split(" ")
            deserializedChecksumBin.append(" ".join(char for char in chars))
            deserializedChecksumBin.append("|")
            deserializedBinData.append("".join(chr(int(char, 2)) for char in chars))
        deserializedChecksumStr = "".join(binary for binary in deserializedChecksumBin)
        deserializedChecksum = hashCompute(deserializedChecksumStr)
        if realChecksum != deserializedChecksum:
            print("[-] Checksum hash verification failed. Data has been tampered!!")
            return -1
        if not deserializedBinData:
            print("[-] Binary Deserialization failed!!")
            return -1
        print("[+] Binary data Deserialized successfully!")
    return deserializedBinData


serializeBinData("test.bin", ["1:Tron:20000", "2:Grim:10000",
                 "3:Joe:28000", "4:John:30000", "5:Doe:5000"])

data = deserializeBinData("test.bin")
print(data)

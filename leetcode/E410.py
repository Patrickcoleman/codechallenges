def readBinaryWatch(turnedOn: int):
        outputs = []
        for h in range(12):
            for m in range(60):
                binaryh = bin(h).count("1")
                binarym = bin(m).count("1")
                if binarym + binaryh == turnedOn:
                     outputs.append(str(h) + ":" + ("0" if m < 10 else "") + str(m))
        
        return outputs


print(readBinaryWatch(5))
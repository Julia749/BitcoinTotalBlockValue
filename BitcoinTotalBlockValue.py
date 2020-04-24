from bitcoin.rpc import RawProxy

p = RawProxy()
startBlock = 0
endBlock = 0
option = 0
heightOfBlock = 0
totalBlocks = 0
totalValue = 0
maximum = 0
minimum = 0
average = 0
index = 0
label0 = "############################################################################################################"
label1 = "------------------------------------------------------------------------------------------------------------"
label2 = "============================================================================================================"

print(label2)
print("Program to analyse the bitcoin block values.")
print("After you have entered the start and end block number (height of the blocks) you can choose weather you want")
print(" the maximum block value, the minimum block value or the average value of the blocks")
print(label2)

print("Write in the Start and End Block a Value (for example 378314):")
startBlock = int(input("Enter start Block height: "))

if startBlock > 0:
    endBlock = int(input("Enter end Block height:   "))
elif startBlock > 700000:
    print("Warning: Start Block is bigger then 700.000")
    print(label0)
else:
    print("Warning: Start Block is smaller then 1")
    print(label0)

if endBlock > 0:
    print(label0)
    print("Options:")
    print("Option 1: Total value of all blocks")
    print("Option 2: Maximum block value")
    print("Option 3: Minimum block value")
    print("Option 4: Average value of the blocks")
elif endBlock > 700000:
    print("Warning: end block is bigger then 700.000")
    print(label0)
    print("")
else:
    print("Warning: end block is smaller then 1")
    print(label0)
    print("")

if endBlock >= startBlock:
    totalBlocks = endBlock - startBlock
else:
    print("Warning: end block is smaller then start block")
    print(label0)
    print("")

option = int(input("Choose an option: "))
print(label0)

while index <= totalBlocks:
    blockValue = 0
    heightOfBlock = startBlock + index

    blockHash = p.getblockhash(heightOfBlock)
    block = p.getblock(blockHash)

    transactions = block['tx']

    for txid in transactions:
        transactionValue = 0

        rawTransactions = p.getrawtransaction(txid)
        decoded_tx = p.decoderawtransaction(rawTransactions)

        for output in decoded_tx['vout']:
            transactionValue = transactionValue + output['value']

        blockValue = blockValue + transactionValue

    totalValue = totalValue + blockValue

    if index == 0:
        minimum = blockValue
    if blockValue < minimum:
        minimum = blockValue
    if blockValue > maximum:
        maximum = blockValue

    average = totalValue / (totalBlocks + 1)

    singleBlock = "Total value of block with height"
    multiBlock = "Total value of all blocks"
    maxBlock = "The maximum block value is"
    minBlock = "The minimum block value is"
    avgBlock = "The average from all chosen block values is"
    unit = "BTC"

    print(singleBlock, heightOfBlock, ": ", round(blockValue, 2), unit)

    index +=1

if option == 1:
    print(label1)
    print(multiBlock, ":", round(totalValue, 2), unit)
elif option == 2:
    print(label1)
    print(maxBlock, ":", round(maximum, 2), unit)
elif option == 3:
    print(label1)
    print(minBlock, ":", round(minimum, 2), unit)
elif option == 4:
    print(label1)
    print(avgBlock, ":", round(average, 2), unit)
else:
    print(label1)
    print ("Option ", option, " is invalid")

print(label0)
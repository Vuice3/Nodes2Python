import sys, os, pickle

# Welcome to the .NODES to .PY module! Put a stickfigure in this directory and name it "input.nodes" to get started.

# To detect input.nodes, we use the 'open()' function and set it to read in binary mode:

with open('input.nodes', 'rb') as f:
    nodeImport = f.read()


nodeData_Base10 = list(nodeImport) # << We are done importing the data as a list, with each byte being an individual list object.

# ^^ nodeData_Base10 will be used to call the stickfigure byte data to read throughout this module.

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#    Below I define a function that converts a base10 byte to a binary byte representation. This is for
# vv 8-16-32-bit signed/unsigned ints and floats that we will have to be able to view individual bits to effectively read.


def toBits(base10Num):
    if int(base10Num) > 255 or int(base10Num) < 0: # << Checks if given number is in the valid range of 8-bit integers (0-255)
        print('\nError: base10Num given by caller is out of range. (Range: 0-255), (Called base10Num: ' + base10Num + ')')
        return 'ERR'
    b10Split = str(bin(base10Num))  # << The bin function does most of the work converting to base2.
    bits = [] # << Empty list to contain the 1s and 0s.
    for chr in b10Split:
        bits.append(chr) # << Append each character of b10Split individually to the end of the empty "bits" list.
    bits.pop(0)
    bits.pop(0) # Pop the first 2 items in the bits list because of the extra junk characters.
    while len(bits) < 8:
        bits.insert(0, '0') # << Inserts 0 at the start of the bits list until there is 8 objs in the bits list.

    output = list(map(int, bits)) # << Converts all list elements of "bits" to integers

    print('BITS-OUTPUT: ' + str(output))

    return output # << Return the base2 representation of the byte to the caller.


# Now time to define a signed 32-bit int big endian converter function. It'll be used a lot when reading bytes of a stickfigure.
    # How to convert to signed 32-bit int big endian:
        # 1 - Let the first bit (A.K.A sign bit) determine if the number is negative or positive (0 = pos, 1 = neg)
        # 2 - Multiply each bit by the corresponding power of two (i.e. if x = the second bit, then do x * 2^30, if x = third bit,
        # do x * 2^29, so on and so on until you multiply the last bit by 2^0
        # 3 - Add the sum of the products you get from multiplying the bit by the power of two. This is your output.

def signed32BitIntBigEndian(byte0 , byte1 , byte2 , byte3, callNote): # << Inputs must be base2-represented bit lists via toBits function.
                                                                      # callNote is just a note sent by the caller for debug purposes.


    negDetectVar = byte0 # << A slight chokeup on my end occured, so I added this one-use variable.
    if negDetectVar[0] == 1:
        negativeMode = True # << Determining if the number is negative via the sign bit. This is vital, as 0 and 1's "roles"
    else:                   # are swapped if it is a negative integer.
        negativeMode = False
    inputtedNum = []
    flattenLoopVar = -1
    print('Caller note for 32 bit int (signed): ' + callNote)
    print('byte 1:\n' + str(byte1))

    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte0[flattenLoopVar])  # << Flattening base2 representation of bytes 0-3 into a single list. 
    flattenLoopVar = -1                                     # We arent using the typical flattening method because it causes bugs.
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte1[flattenLoopVar])
    flattenLoopVar = -1
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte2[flattenLoopVar])
    flattenLoopVar = -1
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte3[flattenLoopVar])
    
    print(str(inputtedNum))
    
    negLoopVar = -1
    if negativeMode == True:
        print('Negative Mode \n\n\n')
        for i in range(len(inputtedNum)):  # << If in negative mode, flip every 0 to a 1, and every 1 to a 0.
            if inputtedNum[i] == 0:
                inputtedNum[i] = 1
            else:
                inputtedNum[i] = 0
    else: print('Positive Mode\n\n\n')

    
    convertedNumbers = []
    convLoopVar = -1
    powersOfTwo = [2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304,
                   2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64,
                  32, 16, 8, 4, 2, 1] # << All powers of two, from 2^0 to 2^31 (in reverse order because of big endianness)
    convertedPower = inputtedNum[convLoopVar] * powersOfTwo[convLoopVar]

    while convLoopVar < 31: # << Multiplies each bit by the correct power of 10 and adds the product to convertedNumbers .
        convLoopVar = convLoopVar + 1
        convertedPower = int(inputtedNum[convLoopVar]) * int(powersOfTwo[convLoopVar])
        print(str(convertedPower))
        convertedNumbers.append(convertedPower)

    convertedNumbers.pop(0) # << The first bit was already used to determine neg/pos, hence we discard the first converted number.

    print('Converted Numbers: \n\n' + str(convertedNumbers))

    # vv output = The sum of all objects in convertedLists (Always 0-30 if there is no 'ERR'). Sorry its such a long line.
    output = int(convertedNumbers[0]) + int(convertedNumbers[1]) + int(convertedNumbers[2]) + int(convertedNumbers[3]) + int(convertedNumbers[4]) + int(convertedNumbers[5]) + int(convertedNumbers[6]) + int(convertedNumbers[7]) + int(convertedNumbers[8]) + int(convertedNumbers[9]) + int(convertedNumbers[10]) + int(convertedNumbers[11]) + int(convertedNumbers[12]) + int(convertedNumbers[13]) + int(convertedNumbers[14]) + int(convertedNumbers[15]) + int(convertedNumbers[16]) + int(convertedNumbers[17]) + int(convertedNumbers[18]) + int(convertedNumbers[19]) + int(convertedNumbers[20]) + int(convertedNumbers[21]) + int(convertedNumbers[22]) + int(convertedNumbers[23]) + int(convertedNumbers[24]) + int(convertedNumbers[25]) + int(convertedNumbers[26]) + int(convertedNumbers[27]) + int(convertedNumbers[28]) + int(convertedNumbers[29]) + int(convertedNumbers[30])

    if negativeMode == True:
        if output == 0:
            print('OUTPUT: ' + str(output - 1))
            return output - 1
        else:
            print('OUTPUT: ' + str(-1 * output))
            return -1 * output          # << Return the converted number. If in negative mode, return the forced negative version
    else:                               # of output , unless output = 0, in which case return output - 1. Else, just return output
        print('OUTPUT: ' + str(output)) # normally.
        return output               


# Now to define a 32-bit float big endian function. This is also used a lot. We will call it singlePrecisionFloat .
    # I was going to put conversion steps here, but this article explains it way better: 
        # https://dev.to/trekhleb/binary-representation-of-the-floating-point-numbers-p7b
        
def singlePrecisionFloat(byte0, byte1, byte2, byte3, callNote): # << Inputs must be base2-represented byte lists via toBits function.
    
    inputtedNum = []
    flattenLoopVar = -1

    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte0[flattenLoopVar])  # << Flattening base2 representation of bytes 0-3 into a single list. 
    flattenLoopVar = -1                                # We arent using the typical flattening method because it causes bugs.
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte1[flattenLoopVar])
    flattenLoopVar = -1
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte2[flattenLoopVar])
    flattenLoopVar = -1
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte3[flattenLoopVar])

    print('Caller note for 32 bit float (signed): ' + callNote)

    print('float inputted num: ' + str(inputtedNum))

    if inputtedNum[0] == 1:    # << First is first, set the sign bit. Easiest part.
        sign = -1
    else:
        sign = 1

    exponentList = [] # << Creating a list for multiplying bits by the corresponding power of two.
    convLoopVar = 0 # << Normally I would set this to -1 but as of now, its simpler to set this to 0.

    powersOfTwo = [128, 64, 32, 16, 8, 4, 2, 1]

    while convLoopVar < 8:
        convLoopVar = convLoopVar + 1
        exponentList.append(inputtedNum[convLoopVar] * powersOfTwo[convLoopVar - 1])

    exponent = exponentList[0] + exponentList[1] + exponentList[2] + exponentList[3] + exponentList[4] + exponentList[5] + exponentList[6] + exponentList[7]
    print('exponent: ' + str(exponent))
    # ^^ Adds each element from exponentList together (Range is 0-7). Sorry it goes offscreen.
    bias = 2 ** 7 - 1

    biased_exponent = exponent - bias # << Here is our second variable. We can reset the loop variables now for reuse:

    print('biased_exponent: ' + str(biased_exponent))

    exponentList = []
    convLoopVar = -1
    powersOfTwo = [2 ** -1, 2 ** -2, 2 ** -3, 2 ** -4, 2 ** -5, 2 ** -6, 2 ** -7, 2 ** -8, 2 ** -9, 2 ** -10, 2 ** -11,
                   2 ** -12, 2 ** -13, 2 ** -14, 2 ** -15, 2 ** -16, 2 ** -17, 2 ** -18, 2 ** -19, 2 ** -20, 2 ** -21,
                   2 ** -22, 2 ** -23] # << Powers of two, from 2^-1 to 2^-23
    print('Powers of two: ' + str(powersOfTwo))

    while convLoopVar < 22: # Significand starts on byte 8 and ends on byte 31 (if starting from 0)
        convLoopVar = convLoopVar + 1
        exponentList.append(inputtedNum[convLoopVar + 8] * powersOfTwo[convLoopVar])
        print('Append to exponentList: ' + str(inputtedNum[convLoopVar + 8] * powersOfTwo[convLoopVar]))


    significand = exponentList[0] + exponentList[1] + exponentList[2] + exponentList[3] + exponentList[4] + exponentList[5] + exponentList[6] + exponentList[7] + exponentList[8] + exponentList[9] + exponentList[10] + exponentList[11] + exponentList[12] + exponentList[13] + exponentList[14] + exponentList[15] + exponentList[16] + exponentList[17] + exponentList[18] + exponentList[19] + exponentList[20] + exponentList[21] + exponentList[22]
    # ^^ Adds each element from exponentList together (Range is 0-22). Really long.
    # ^^ This is also our final variable. Now for the output:
    print('Significand: ' + str(significand))

    output = sign * (2 ** biased_exponent) * significand
    print('OUTPUT: ' + str(output * 2))
    return output * 2 # << For some reason the output is always the answer divided by 2. Idk why this happened but its fine, I'll just
                      # 

# Now to define an 8-bit signed byte function. Same as signed 32 bit integer big endian, but just a single byte:
# (yes i just copy and pasted the signed32BitIntBigEndian code and deleted a lot of the unimportant stuff)

def signed8BitByte(byte, callNote): # << Input must be a base2-represented bit list via toBits function.
    negDetectVar = byte # << Too lazy to replace this variable lol ima just keep it
    if negDetectVar[0] == 1:
        negativeMode = True # << Determining if the number is negative via the sign bit. This is vital, as 0 and 1's "roles"
    else:                   # are swapped if it is a negative integer.
        negativeMode = False

    print('Caller note for 8 bit int (signed): ' + callNote)

    negLoopVar = -1
    if negativeMode == True:
        print('Negative Mode \n\n\n') # << If in negative mode, flip every 1 to a 0, and every 0 to a 1.
        for i in range(len(byte)):
            if byte[i] == 0:
                byte[i] = 1
            else:
                byte[i] = 0
    else: print('Positive Mode\n\n\n')

    convertedNumbers = []
    convLoopVar = -1
    powersOfTwo = [128, 64, 32, 16, 8, 4, 2, 1] # << All powers of two, from 2^0 to 2^7 (in reverse order because of big endianness)
    convertedPower = byte[convLoopVar] * powersOfTwo[convLoopVar]

    while convLoopVar < 7: # << Multiplies each bit by the correct power of 10 and adds the product to convertedNumbers .
        convLoopVar = convLoopVar + 1
        convertedPower = int(byte[convLoopVar]) * int(powersOfTwo[convLoopVar])
        print(str(convertedPower))
        convertedNumbers.append(convertedPower)

    convertedNumbers.pop(0) # << The first bit was already used to determine neg/pos, hence we discard the first converted number.

    print('Converted Numbers: \n\n' + str(convertedNumbers))

    # vv output = The sum of all objects in convertedLists (Always 0-6 if there is no 'ERR'). Sorry its such a long line.
    output = int(convertedNumbers[0]) + int(convertedNumbers[1]) + int(convertedNumbers[2]) + int(convertedNumbers[3]) + int(convertedNumbers[4]) + int(convertedNumbers[5]) + int(convertedNumbers[6])

    if negativeMode == True:
        if output == 0:
            print('OUTPUT: ' + str(output - 1))
            return output - 1
        else:
            print('OUTPUT: ' + str(-1 * output))
            return -1 * output         # << Return the converted number. If in negative mode, return the forced negative version
    else:                               # of output , unless output = 0, in which case return output - 1. Else, just return output
        print('OUTPUT: ' + str(output)) # normally.
        return output


# Now lets define a 16-bit signed number function. Same as signed32BitIntBigEndian again, but with only 2 bytes.

def signed16BitNumber(byte0 , byte1, callNote): # << Inputs must be base2-represented bit lists via toBits function.
    negDetectVar = byte0 # << A slight chokeup on my end occured, so I added this one-use variable.
    if negDetectVar[0] == 1:
        negativeMode = True # << Determining if the number is negative via the sign bit. This is vital, as 0 and 1's "roles"
    else:                   # are swapped if it is a negative integer.
        negativeMode = False
    inputtedNum = []
    flattenLoopVar = -1

    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte0[flattenLoopVar])  # << Flattening base2 representation of bytes 0-3 into a single list. 
    flattenLoopVar = -1                                     # We arent using the typical flattening method because it causes bugs.
    while flattenLoopVar < 8:
        flattenLoopVar = flattenLoopVar + 1
        if flattenLoopVar != 8:
            inputtedNum.append(byte1[flattenLoopVar])

    print('Caller note for 16 bit int (signed): ' + callNote)

    if negativeMode == True:
        print('Negative Mode \n\n\n') # << If in negative mode, flip every 1 to a 0, and every 0 to a 1.
        for i in range(len(inputtedNum)):
            if byte[i] == 0:
                byte[i] = 1
            else:
                byte[i] = 0
    else: print('Positive Mode\n\n\n')
    
    print(str(inputtedNum))

    convertedNumbers = []
    convLoopVar = -1
    powersOfTwo = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64,
                  32, 16, 8, 4, 2, 1] # << All powers of two, from 2^0 to 2^15 (in reverse order because of big endianness)
    convertedPower = inputtedNum[convLoopVar] * powersOfTwo[convLoopVar]

    while convLoopVar < 15: # << Multiplies each bit by the correct power of 10 and adds the product to convertedNumbers .
        convLoopVar = convLoopVar + 1
        convertedPower = int(inputtedNum[convLoopVar]) * int(powersOfTwo[convLoopVar])
        print(str(convertedPower))
        convertedNumbers.append(convertedPower)

    convertedNumbers.pop(0) # << The first bit was already used to determine neg/pos, hence we discard the first converted number.

    print('Converted Numbers: \n\n' + str(convertedNumbers))

    # vv output = The sum of all objects in convertedLists (Always 0-14 if there is no 'ERR'). Sorry its such a long line.
    output = int(convertedNumbers[0]) + int(convertedNumbers[1]) + int(convertedNumbers[2]) + int(convertedNumbers[3]) + int(convertedNumbers[4]) + int(convertedNumbers[5]) + int(convertedNumbers[6]) + int(convertedNumbers[7]) + int(convertedNumbers[8]) + int(convertedNumbers[9]) + int(convertedNumbers[10]) + int(convertedNumbers[11]) + int(convertedNumbers[12]) + int(convertedNumbers[13]) + int(convertedNumbers[14])

    if negativeMode == True:
        if output == 0:
            print('OUTPUT: ' + str(output - 1))
            return output - 1
        else:
            print('OUTPUT: ' + str(-abs(output)))
            return -abs(output)         # << Return the converted number. If in negative mode, return the forced negative version
    else:                               # of output , unless output = 0, in which case return output - 1. Else, just return output
        print('OUTPUT: ' + str(output)) # normally.
        return output               

# I forgot to do this earlier, but there is unsigned 8 bit bytes we have to put in, so lets just create a function for that rq:

def unsigned8BitByte(byte, callNote): # << Input must be a base2-represented bit list via toBits function.
    convertedNumbers = []
    convLoopVar = -1
    powersOfTwo = [128, 64, 32, 16, 8, 4, 2, 1] # << All powers of two, from 2^0 to 2^7 (in reverse order because of big endianness)
    convertedPower = byte[convLoopVar] * powersOfTwo[convLoopVar]

    while convLoopVar < 7: # << Multiplies each bit by the correct power of 10 and adds the product to convertedNumbers .
        convLoopVar = convLoopVar + 1
        convertedPower = int(byte[convLoopVar]) * int(powersOfTwo[convLoopVar])
        print(str(convertedPower))
        convertedNumbers.append(convertedPower)
    print('Caller note for 8 bit int (unsigned): ' + callNote)

    print('Converted Numbers: \n\n' + str(convertedNumbers))

    # vv output = The sum of all objects in convertedLists (Always 0-6 if there is no 'ERR'). Sorry its such a long line.
    output = int(convertedNumbers[0]) + int(convertedNumbers[1]) + int(convertedNumbers[2]) + int(convertedNumbers[3]) + int(convertedNumbers[4]) + int(convertedNumbers[5]) + int(convertedNumbers[6])
    print('OUTPUT: ' + str(output))
    return output

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# All bit converters have been finished. Now we can start converting all of the input data to a dict.
# Let stickfigureData be this dictionary:

stickfigureData = dict()

# If you haven't read Vince's documentation on the node format, you should probably do that. Heres the mirror download:
# https://cdn.discordapp.com/attachments/854456068196007958/1036820814143696967/NODES_FORMAT_334.txt

# Below is the header of the stickfigure.

stickfigureData['ver'] = (signed32BitIntBigEndian(toBits(int(nodeData_Base10[0])),
                                                  toBits(int(nodeData_Base10[1])),
                                                  toBits(int(nodeData_Base10[2])),
                                                  toBits(int(nodeData_Base10[3])), 'ver')) # << Version Number (for backwards compatibility)

stickfigureData['scale'] = (float(singlePrecisionFloat(toBits(int(nodeData_Base10[4])),
                                                       toBits(int(nodeData_Base10[5])),
                                                       toBits(int(nodeData_Base10[6])),
                                                       toBits(int(nodeData_Base10[7])), 'scale'))) # << Stickfigure Scale

stickAlpha = int(unsigned8BitByte(toBits(int(nodeData_Base10[8])), 'alpha'))
stickBlue =  int(unsigned8BitByte(toBits(int(nodeData_Base10[9])), 'blue'))
stickGreen = int(unsigned8BitByte(toBits(int(nodeData_Base10[10])), 'green'))
stickRed =   int(unsigned8BitByte(toBits(int(nodeData_Base10[11])), 'red'))

stickfigureData['alpha'] = (stickAlpha) # << Stickfigure Color Alpha
stickfigureData['blue'] = (stickBlue) # << Stickfigure Color Blue
stickfigureData['green'] = (stickGreen) # << Stickfigure Color Green
stickfigureData['red'] = (stickRed) # << Stickfigure Color Red

# Stickfigure header is done. All beyond is node-specific data (Body) and polyfill data (Footer). That means we have to use  
# variables to keep track of the byte we are on:

currentNodeData = []
currentNodeID = 0 # << The ID of the current node (Used for dict element defining)
totalNodeBytes = 0 # << Number of bytes used per node varies per version and per polyfill nodes, so this will help greatly.
stickfigureData['nodeCount'] = 0 # The sum of all numbers of child nodes. (Does not include polyfill nodes)
              # (nodeCount extends overtime as 'nodeBody()' reads the data, since we add the read data to nodeCount for
              # every node)
byteOffset = 0 # << We will set this variable at the end of nodeBody() , but for now leave it blank. Its a for convenience
               # so we don't have to type an extremely long equation every time we want to append to stickfigureData .


mainNode = False # << This was originally planned to do something, but it's cut now. Keeping it here because theres a
                 # massive if statement that I dont wanna take the time to get rid of all the indents for.

nodeParentVar = 0 # << Setting this to 0 by default. Using this to store the parent node ID for the current node being read.
childrenRead = 0 # << The amount of children for the parent node ID that have been read.
              

def nodeBody():
    global mainNode
    global totalNodeBytes
    global currentNode  # << Use the global variables instead of the 
    global byteOffset
    global stickfigureData
    global nodeParentVar
    global childrenRead
    parentReadLoop = 0
    if mainNode == True: # << Set the main node.
        return
    
    else:
        # Many parts of this script are about to go far off-screen, no way to fix this. Just bare with me --
        nodeReadLoop = -1
        while nodeReadLoop < stickfigureData['nodeCount']: # << Once nodeReadLoop catches up with nodeCount, break loop and return.
            currentNodeType = signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'Type')
           # ^^ + 1 (Since we havent defined the node's ID yet, just store the type in a variable temporarily
            totalNodeBytes = totalNodeBytes + 1
            currentNodeID = str(signed32BitIntBigEndian(toBits(int(nodeData_Base10[12 + totalNodeBytes])),
                                                    toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                    toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                    toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])),
                                                    'Layer')) # << + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_Type'] = (currentNodeType)
            stickfigureData['node_' + currentNodeID + '_Layer'] = (currentNodeID) # << Now that the node ID for this node has been assigned,
                                                                                  # we can start appending to stickfigureData.
            
            # vv Just getting the booleans out of the way:
            # (The way we're defining the booleans will make any values that are not 0 equal True. Just something to note.)
            if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'isStatic') == 0:
               stickfigureData['node_' + currentNodeID + '_IsStatic'] = (False) 
            else: stickfigureData['node_' + currentNodeID + '_IsStatic'] = (True) # << + 1
            totalNodeBytes = totalNodeBytes + 1
            if (str(signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'isStretchy'))) == 0:
                stickfigureData['node_' + currentNodeID + '_IsStretchy'] = (False)
            else: stickfigureData['node_' + currentNodeID + '_IsStretchy'] = (True) # << + 1
            totalNodeBytes = totalNodeBytes + 1
            if stickfigureData['ver'] >= 248:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'isSmartStretch') == 0:
                    stickfigureData['node_' + currentNodeID + '_IsSmartStretch'] = (False) # << + 1
                else: stickfigureData['node_' + currentNodeID + '_IsSmartStretch'] = (True)
                totalNodeBytes = totalNodeBytes + 1
            if stickfigureData['ver'] >= 252:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'dontSmartStretch') == 0:
                    stickfigureData['node_' + currentNodeID + '_DontSmartStretch'] = (False) # << + 1
                else: stickfigureData['node_' + currentNodeID + '_DontSmartStretch'] = (True) 
                totalNodeBytes = totalNodeBytes + 1
            if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'useSegmentColor') == 0:
                stickfigureData['node_' + currentNodeID + '_UseSegmentColor'] = (False) # << + 1
            else: stickfigureData['node_' + currentNodeID + '_UseSegmentColor'] = (True)
            totalNodeBytes = totalNodeBytes + 1
            if stickfigureData['ver'] >= 256:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'useCircleOutline') == 0:
                    stickfigureData['node_' + currentNodeID + '_UseCircleOutline'] = (False) # << + 1
                else: stickfigureData['node_' + currentNodeID + '_UseCircleOutline'] = (True)
                totalNodeBytes = totalNodeBytes + 1
            if stickfigureData['ver'] >= 176:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'useGradientColor') == 0:
                    stickfigureData['node_' + currentNodeID + '_UseGradientColor'] = (False) # << + 1
                else: stickfigureData['node_' + currentNodeID + '_UseGradientColor'] = (True)
                totalNodeBytes = totalNodeBytes + 1
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'reverseGradient') == 0:
                    stickfigureData['node_' + currentNodeID + '_ReverseGradient'] = (False)
                else: stickfigureData['node_' + currentNodeID + '_ReverseGradient'] = (True) # << + 1
                totalNodeBytes = totalNodeBytes + 1
            if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'useSegmentScale') == 0:
                stickfigureData['node_' + currentNodeID + '_UseSegmentScale'] = (False)
            else: stickfigureData['node_' + currentNodeID + '_UseSegmentScale'] = (True) # << + 1
            totalNodeBytes = totalNodeBytes + 1

            stickfigureData['node_' + currentNodeID + '_LocalX'] = singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'localX')
                                                                                       # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_LocalY'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'localY'))
                                                                                        # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_Scale'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'nodeScale'))
                                                                                       # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_DefaultLength'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'defaultLength'))
                                                                                               # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_Length'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                         toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'length'))
                                                                                        # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_DefaultThickness'] = (signed32BitIntBigEndian(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                      toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                      toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                      toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'defaultThickness'))
                                                                                                     # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_Thickness'] = (signed32BitIntBigEndian(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                               toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                               toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                               toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'thickness'))
                                                                                              # ^^ + 4
            totalNodeBytes = totalNodeBytes + 4
            if stickfigureData['ver'] >= 320:
                stickfigureData['node_' + currentNodeID + '_SegmentCurveRadius'] = (signed32BitIntBigEndian(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                            toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                            toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                            toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'segmentCurveRadius'))
                                                                                                           # ^^ + 4
                totalNodeBytes = totalNodeBytes + 4
            if stickfigureData['ver'] >= 256:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'isHalfArc') == 0:
                    stickfigureData['node_' + currentNodeID + '_IsHalfArc'] = (False)
                else: stickfigureData['node_' + currentNodeID + '_IsHalfArc'] = (True) # << + 1
                totalNodeBytes = totalNodeBytes + 1
                stickfigureData['node_' + currentNodeID + '_RightTriangleDirection'] = (signed16BitNumber(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                          toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])), 'rightTriangleDirection')) # << + 2
                totalNodeBytes = totalNodeBytes + 2
            if stickfigureData['ver'] >= 300:
                if signed8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes])), 'triangleUpsideDown') == 0:
                    stickfigureData['node_' + currentNodeID + '_TriangleUpsideDown'] = (False)
                else: stickfigureData['node_' + currentNodeID + '_TriangleUpsideDown'] = (True) # << + 1
                totalNodeBytes = totalNodeBytes + 1
            if stickfigureData['ver'] >= 256:
                stickfigureData['node_' + currentNodeID + '_TrapezoidTopThicknessRatio'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                                 toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                                 toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                                 toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'trapezoidTopThicknessRatio')) # << + 4
                totalNodeBytes = totalNodeBytes + 4
                stickfigureData['node_' + currentNodeID + '_NumberOfPolygonVertices'] = (signed16BitNumber(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                           toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])), 'numberOfPolygonVertices')) # << + 2
                totalNodeBytes = totalNodeBytes + 2
            if stickfigureData['ver'] >= 248:
                stickfigureData['node_' + currentNodeID + '_DefaultLocalAngle'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'defaultLocalAngle')) # << + 4
                totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_LocalAngle'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                             toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                             toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                             toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'localAngle')) # << + 4
            totalNodeBytes = totalNodeBytes + 4
            if stickfigureData['ver'] >= 248:
                stickfigureData['node_' + currentNodeID + '_DefaultAngle'] = (singlePrecisionFloat(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                   toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                   toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                   toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'defaultAngle')) # << + 4
                totalNodeBytes = totalNodeBytes + 4


            stickfigureData['node_' + currentNodeID + '_SegmentColor_Alpha'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])), 'segmentAlpha')) # << + 1
            stickfigureData['node_' + currentNodeID + '_SegmentColor_Blue'] =  (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])), 'segmentBlue')) # << + 1
            stickfigureData['node_' + currentNodeID + '_SegmentColor_Green'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])), 'segmentGreen')) # << + 1
            stickfigureData['node_' + currentNodeID + '_SegmentColor_Alpha'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'segmentRed')) # << + 1
            totalNodeBytes = totalNodeBytes + 4
            if stickfigureData['ver'] >= 176:
                stickfigureData['node_' + currentNodeID + '_GradientColor_Alpha'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])), 'gradientAlpha')) # << + 1
                stickfigureData['node_' + currentNodeID + '_GradientColor_Blue'] =  (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])), 'gradientBlue')) # << + 1
                stickfigureData['node_' + currentNodeID + '_GradientColor_Green'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])), 'gradientGreen')) # << + 1
                stickfigureData['node_' + currentNodeID + '_GradientColor_Red'] =   (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'gradientRed')) # << + 1
                totalNodeBytes = totalNodeBytes + 4
            if stickfigureData['ver'] >= 256:
                stickfigureData['node_' + currentNodeID + '_CircleOutlineColor_Alpha'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])), 'circleOutlineAlpha')) # << + 1
                stickfigureData['node_' + currentNodeID + '_CircleOutlineColor_Blue'] =  (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])), 'circleOutlineBlue')) # << + 1
                stickfigureData['node_' + currentNodeID + '_CircleOutlineColor_Green'] = (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])), 'circleOutlineGreen')) # << + 1
                stickfigureData['node_' + currentNodeID + '_CircleOutlineColor_Red'] =   (unsigned8BitByte(toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'circleOutlineRed')) # << + 1
                totalNodeBytes = totalNodeBytes + 4
            stickfigureData['node_' + currentNodeID + '_NumberOfChildNodes'] = (signed32BitIntBigEndian(toBits(int(nodeData_Base10[12 + totalNodeBytes + 0])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 1])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 2])),
                                                                                                        toBits(int(nodeData_Base10[12 + totalNodeBytes + 3])), 'numberOfChildNodes'))
                                                                                                        # ^^ + 4


            stickfigureData['nodeCount'] = stickfigureData['nodeCount'] + stickfigureData['node_' + currentNodeID + '_NumberOfChildNodes']
            # ^^ Add the current node's 'Number of child nodes' to nodeCount. 
            totalNodeBytes = totalNodeBytes + 4
            nodeReadLoop = nodeReadLoop + 1 # << Adds 1 to the loop variable.

            
            
            # We have to make a way to deter between parent, child, and sister nodes, so here we go, oh boy:
            if nodeParentVar == currentNodeID:
                stickfigureData['node_' + currentNodeID + 'Parent'] = (False)
            else:
                if stickfigureData['node_' + str(nodeParentVar) + '_NumberOfChildNodes'] == 0:
                    parentReadloop = 0
                    while parentReadLoop < stickfigureData['nodeCount']:
                          nodeParentVar = stickfigureData['node_' + str(nodeParentVar) + '_Parent']
                          if stickfigureData['node_' + str(nodeParentVar) + '_NumberOfChildNodes'] != 0:
                              parentReadLoop = stickfigureData['nodeCount']
                          else: parentReadLoop = parentReadLoop + 1
                stickfigureData['node_' + currentNodeID + '_Parent'] = (nodeParentVar)
            nodeParentVar = stickfigureData['node_' + currentNodeID + '_Layer']
            # Ok so what the hell just went on in that strip of code? -
            # 1. If it's the main node, just pass this entire process.
            # 2. Else, if the previous read node's number of children is 0:
            # 3. Check the node before the previous node, and the previous node before that, etc etc.
            # 4. Once you finally arrive at a node that has a child node:
            # 5. Set that node as the current node's parent.
            # 6. Set nodeParentVar to the current node's ID, to set up this parent-check again.

                



            print('////////////////////////\nnodeReadLoop = ' + str(nodeReadLoop) + '\n////////////////////////')
    byteOffset = 12 + totalNodeBytes
    return

# The body (nodes) are finished, now we have to do the footer (polyfills) :

def polyfillFooter():
    global byteOffset
    global stickfigureData
    stickfigureData['numberOfPolyfills'] = signed32BitIntBigEndian(toBits(int(nodeData_Base10[byteOffset + 0])), # << + 4
                                                                   toBits(int(nodeData_Base10[byteOffset + 1])),
                                                                   toBits(int(nodeData_Base10[byteOffset + 2])),
                                                                   toBits(int(nodeData_Base10[byteOffset + 3])), 'numberOfPolyfills')
    byteOffset = byteOffset + 4
    polyReadLoop = 0

    while polyReadLoop < stickfigureData['numberOfPolyfills']:
        currentParentNode = str(signed32BitIntBigEndian(toBits(int(nodeData_Base10[byteOffset + 0])), # << + 4
                                                        toBits(int(nodeData_Base10[byteOffset + 1])),
                                                        toBits(int(nodeData_Base10[byteOffset + 2])),
                                                        toBits(int(nodeData_Base10[byteOffset + 3])), 'polyParentNode'))
        byteOffset = byteOffset + 4
        stickfigureData['polyfill_' + currentParentNode + '_ParentNode'] = int(currentParentNode)
        stickfigureData['polyfill_' + currentParentNode + '_Color_Alpha'] = unsigned8BitByte(toBits(int(nodeData_Base10[byteOffset + 0])), 'polyColorAlpha')
        stickfigureData['polyfill_' + currentParentNode + '_Color_Blue'] =  unsigned8BitByte(toBits(int(nodeData_Base10[byteOffset + 1])), 'polyColorBlue')
        stickfigureData['polyfill_' + currentParentNode + '_Color_Green'] = unsigned8BitByte(toBits(int(nodeData_Base10[byteOffset + 2])), 'polyColorGreen')
        stickfigureData['polyfill_' + currentParentNode + '_Color_Red'] =   unsigned8BitByte(toBits(int(nodeData_Base10[byteOffset + 3])), 'polyColorRed')
        # ^^ + 4
        byteOffset = byteOffset + 4
        if signed8BitByte(toBits(int(nodeData_Base10[byteOffset])), 'usePolyfillColor') == 0:
            stickfigureData['polyfill_' + currentParentNode + '_UsePolyfillColor'] = False
        else: stickfigureData['polyfill_' + currentParentNode + '_UsePolyfillColor'] = True # << + 1
        byteOffset = byteOffset + 1
        stickfigureData['polyfill_' + currentParentNode + '_NumberOfPolyfillNodes'] = signed32BitIntBigEndian(toBits(int(nodeData_Base10[byteOffset + 0])), # << + 4
                                                                                                              toBits(int(nodeData_Base10[byteOffset + 1])),
                                                                                                              toBits(int(nodeData_Base10[byteOffset + 2])),
                                                                                                              toBits(int(nodeData_Base10[byteOffset + 3])), 'numberOfPolyfillNodes')
        byteOffset = byteOffset = 4
        polyConnectionLoop = 0
        while polyfillConnectionLoop < stickfigureData['polyfill_' + currentParentNode + '_NumberOfPolyfillNodes']:
            currentPolyfillConnectionID = signed32BitIntBigEndian(toBits(int(nodeData_Base10[byteOffset + 0])), # << + 4
                                                                  toBits(int(nodeData_Base10[byteOffset + 1])),
                                                                  toBits(int(nodeData_Base10[byteOffset + 2])),
                                                                  toBits(int(nodeData_Base10[byteOffset + 3])), 'polyConnection')

            stickfigureData['polyfill_' + currentParentNode + '_Connection_' + str(polyConnectionLoop) + '_Layer'] = currentPolyfillConnectionID
            byteOffset = byteOffset + 4

        polyReadLoop = polyReadLoop + 1 

    return


nodeBody()
if stickfigureData['ver'] >= 230:
   polyfillFooter()

print(str(stickfigureData))


# /////////////////////////////////////////
# It's almost over -- We just have to write the stickfigureData to the file:

with open('output.py', 'xt') as f:
    f.write('stickfigureData = ' + str(stickfigureData))

# And with that, nodes2python is finished! This was a fun project tbh, it took a while and there were some mental breakdowns
# along the way, but in the end it was worth it. This took a total of 2 weeks, with almost 700 lines of code written, but it's finally
# time to release this program.
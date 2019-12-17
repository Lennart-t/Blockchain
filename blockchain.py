#Creation of backend
import json
import os
import hashlib

#After creating first block by hand, we wrote create_block function to create the following blocks in the blockchain. The function uses two more functions get_blocks and create_hash, which are defined below.
def create_block(name, birthday, subject, graduation, key):
    #set directory to the blocks directory
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass
    #conduct get_block function, which is defined next
    blocks = get_blocks()
    #as starting block has the name zero, last block's name will always be number of blocks -1     
    last_block = len(blocks) - 1
    #number of new block must be last blocks's number +1
    new_block = str(last_block + 1)

    previous_hash = create_hash(str(last_block))
    #Definition data in each block    
    data = {
                'name': name,
                'date of birth': birthday,
                'study program': subject,
                'date of graduation': graduation,
                'hash': previous_hash
            }
    #With statement to make a new file for new blocks using predefined new_block number as name
    with open(new_block + ".txt", 'w') as txt_file:
        json.dump(data, txt_file, indent=4)

#Function, which sorts blocks and therefore enables us to number blocks in a consecutive number
def get_blocks():
    #set directory to the blocks directory
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass
    #Use of listdir to get all the blocks in our blockchain directory
    blocks = os.listdir()
    #As listdir does not sort blocks, we need to sort all blocks to get the newest one by using list comprehension to return integers for all file names and sort them.
    blocks = sorted(blocks)

    sorted_blocks = []

    for i in range(0, len(blocks)):
        try:
            int(blocks[i][:-4])
        except:
            continue
        sorted_blocks.append(int(blocks[i][:-4]))

    sorted_blocks.sort()
    return sorted_blocks

#Function to create hash for block, by using hashlib module. 
def create_hash(block_name):
    #Function reads the contents of a block and runs them through the SHA-256 hashing algorithm and returns a hash.
    block = open(block_name + ".txt", 'rb')
    block_content = block.read()
    block.close()
    return hashlib.sha256(block_content).hexdigest()

#Function to verify integrity of chain. It does that by verifying the hashes of each block
def verify_chain():
    #Declaring variable blocks that uses predefined function get_blocks() to get all blocks in a sorted order
    blocks = get_blocks()
    results = []
    print(blocks)
    #For loop to iterate through the blocks and read previous blocks' hashes. 
    for block in blocks[2:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        previous_block = str(int(block)-1)
        #Control hash is created - the control hash is implemented by pretending to create a new hash for given block
        true_previous_hash = create_hash(previous_block)
        #If given hash in previous block is equal to controll hash, current hash will be checked, otherwise current block corrupted as previous hash is also corrupted 
        if previous_hash == true_previous_hash:
            #Same control procedure for current hash, same outcome wether hash is corrupted or not
            try:
                next_block = str(int(block) + 1)
                current_hash = create_hash(block)
                true_current_hash = json.load(open(str(next_block) + ".txt"))['hash']
                if current_hash == true_current_hash:
                    result = "a Genuine Block"
                else:
                    result = "a Corrupted Block"
            except:
                result = "a Genuine Block"
        else:
            result = "a Corrupted Block"

        results.append({'block': previous_block, 'result': result})

    results.append({'block': len(blocks) - 1, 'result': "the last bock in the chain: unverifiable"})

    return results

#Function to check if there is a block, which containts data entered by user
def verify_diploma(name, birthday, subject, graduation):
    blocks = get_blocks()
    results = []
    result = "This is a fake diploma!"
    #For loop to open blocks and load respective data
    for block in blocks[1:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        b_name = json.load(open(str(block) + ".txt"))['name']
        b_birthday = json.load(open(str(block) + ".txt"))['date of birth']
        b_subject = json.load(open(str(block) + ".txt"))['study program']
        b_graduation = json.load(open(str(block) + ".txt"))['date of graduation']
        #If statement to compare input of user with data in each block. If one block contains all entered information output to user: genuine diploma, otherwise output: fake diploma
        if b_name == name and b_birthday == birthday and b_subject == subject and b_graduation == graduation:
            previous_block = str(int(block) - 1)
            true_previous_hash = create_hash(previous_block)
            if previous_hash == true_previous_hash:
                try:
                    next_block = str(int(block) + 1)
                    current_hash = create_hash(block)
                    true_current_hash = json.load(open(str(next_block) + ".txt"))['hash']
                    if current_hash == true_current_hash:
                        result = "This is a genuine diploma!"
                        break
                    else:
                        result = "This is a fake diploma!"
                        break
                except:
                    result = "This is a genuine diploma!"
                    break
            else:
                result = "This is a fake diploma!"
                break

    results.append(result)
    return results


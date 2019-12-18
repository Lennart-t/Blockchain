# Creation of back-end mechanics.
import json
import os
import hashlib


# After creating the first block (genesis block) by hand, we wrote create_block() function to create new blocks in
# the blockchain. The function uses two more functions get_blocks() and create_hash(), which are defined below.
def create_block(name, birthday, subject, graduation, key):
    # Set directory to the blocks directory. If not already set.
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass
    # Call get_block() function, which is defined below to retrieve list of blocks.
    blocks = get_blocks()
    # As starting block is named zero ("0"), last block's name will be number of (blocks - 1).
    last_block = len(blocks) - 1
    # Number of new block must be last blocks's number + 1. This needs to be a string as we use it as the name for new block.
    new_block = str(last_block + 1)

    previous_hash = create_hash(str(last_block))
    # Definition of the data structure in each block.
    data = {
                'name': name,
                'date of birth': birthday,
                'study program': subject,
                'date of graduation': graduation,
                'hash': previous_hash
            }
    # With statement to make a new file for new blocks using predefined new_block number as name and data as data.
    with open(new_block + ".txt", 'w') as txt_file:
        json.dump(data, txt_file, indent=4)


# Function get_blocks(), which reads and sorts blocks and therefore enables us to number blocks in a consecutive manner.
def get_blocks():
    # Set directory to the blocks directory. If not already set.
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass
    # Use of listdir to get all the blocks in our blocks directory.
    blocks = os.listdir()

    # As listdir does not sort blocks, we need to sort all blocks to get them in 'chronological' order. We add them
    # to a list as integers (hence, we remove the file extensions).
    sorted_blocks = []

    for i in range(0, len(blocks)):
        try:
            int(blocks[i][:-4])
        except:
            continue
        sorted_blocks.append(int(blocks[i][:-4]))

    sorted_blocks.sort()
    return sorted_blocks


# Function to create hash for the data in each block, by using hashlib module.
def create_hash(block_name):
    # Function reads the contents of a block and runs them through the SHA-256 hashing algorithm and returns this hash.
    block = open(block_name + ".txt", 'rb')
    block_content = block.read()
    block.close()
    return hashlib.sha256(block_content).hexdigest()


# Function to verify the integrity of the blockchain. It does so by verifying the hashes of each block's surrounding blocks.
def verify_chain():
    # Declaring variable blocks that is the output of the previously defined function get_blocks() to get all blocks in a sorted order.
    blocks = get_blocks()
    results = []
    # For-loop to iterate through the blocks and read previous and next blocks' hashes and compare them.

    for block in blocks[2:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        previous_block = str(int(block)-1)
        # Control hash is created - the control hash is implemented by pretending to create a new hash for given block's data.
        true_previous_hash = create_hash(previous_block)
        # If given hash in previous block is equal to control hash, current block content will be compared with next block hash,
        # otherwise current block is corrupted.
        if previous_hash == true_previous_hash:
            # Same control procedure for current block content and next block's hash.
            try:
                next_block = str(int(block) + 1)
                current_hash = create_hash(block)
                true_current_hash = json.load(open(str(next_block) + ".txt"))['hash']
                if current_hash == true_current_hash:
                    result = "a Genuine Block"
                else:
                    result = "a Corrupted Block"
            # If the current block is the last block in the chain, there is no next block, hence the try... except... construction.
            except:
                result = "a Genuine Block"
        else:
            result = "a Corrupted Block"

        # Each result is added to a list of tuples in combination with the number of the block.
        results.append({'block': previous_block, 'result': result})

    results.append({'block': len(blocks) - 1, 'result': "the last bock in the chain: unverifiable"})
    return results


# Function to check if there is a block, which contains the data entered by user on Verify Diploma page.
def verify_diploma(name, birthday, subject, graduation):
    # Declaring variable blocks that is the output of the previously defined function get_blocks() to get all blocks in a sorted order.
    blocks = get_blocks()
    results = []
    result = "This is a fake diploma!"
    # For-loop to open blocks and load respective data.
    for block in blocks[1:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        b_name = json.load(open(str(block) + ".txt"))['name']
        b_birthday = json.load(open(str(block) + ".txt"))['date of birth']
        b_subject = json.load(open(str(block) + ".txt"))['study program']
        b_graduation = json.load(open(str(block) + ".txt"))['date of graduation']

        # If statement to compare input of user with data in each block. If one block contains all entered information,
        # we will check whether it is a genuine block. If so, output to user: genuine diploma, otherwise: fake diploma.
        if b_name == name and b_birthday == birthday and b_subject == subject and b_graduation == graduation:
            previous_block = str(int(block) - 1)
            true_previous_hash = create_hash(previous_block)
            # Same verification procedure as in verify_chain() method above.
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

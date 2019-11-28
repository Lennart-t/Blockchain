import json
import os
import hashlib


def verify_input(payer, amount, receiver):
    if payer == '' or amount == '' or receiver == '':
        return False

    try:
        float(amount)
    except:
        return False

    if float(amount) <= 0:
        return False

    return True


def create_block(payer, amount, receiver):
    if not verify_input(payer, amount, receiver):
        return

    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass

    blocks = get_blocks()
    last_block = len(blocks) - 1

    new_block = str(last_block + 1)

    previous_hash = create_hash(str(last_block))

    data = {
                'payer': payer,
                'amount': amount,
                'payee': receiver,
                'hash': previous_hash
            }

    with open(new_block + ".txt", 'w') as txt_file:
        json.dump(data, txt_file, indent=4)


def get_blocks():
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass

    blocks = os.listdir()

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


def create_hash(block_name):
    block = open(block_name + ".txt", 'rb')
    block_content = block.read()
    block.close()
    return hashlib.sha256(block_content).hexdigest()


def verify_chain():
    blocks = get_blocks()
    results = []
    previous_result = ''

    for block in blocks[1:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']

        previous_block = str(int(block)-1)

        true_hash = create_hash(previous_block)

        if previous_hash == true_hash:
            result = 'a Genuine Block'
        elif previous_result == 'a Corrupted Block':
            result = 'either Genuine or Corrupted, but we do not know for sure (the previous block was fake)'
        else:
            result = 'a Corrupted Block'

        results.append({'block': block, 'result': result})

        previous_result = result

    return results




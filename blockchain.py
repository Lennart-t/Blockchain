import json
import os
import hashlib


def create_block(name, birthday, subject, graduation, key):
    try:
        os.chdir(os.curdir + "/blocks")
    except:
        pass

    blocks = get_blocks()
    last_block = len(blocks) - 1

    new_block = str(last_block + 1)

    previous_hash = create_hash(str(last_block))

    data = {
                'name': name,
                'date of birth': birthday,
                'study program': subject,
                'date of graduation': graduation,
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
    print(blocks)

    for block in blocks[2:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        previous_block = str(int(block)-1)
        true_previous_hash = create_hash(previous_block)

        if previous_hash == true_previous_hash:
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

    results.append({'block': len(blocks) - 1, 'result': "the last bock in the chain: can genuine or fake"})

    return results


def verify_diploma(name, birthday, subject, graduation):
    blocks = get_blocks()
    results = []
    result = "This is a fake diploma!"

    for block in blocks[1:]:
        previous_hash = json.load(open(str(block) + ".txt"))['hash']
        b_name = json.load(open(str(block) + ".txt"))['name']
        b_birthday = json.load(open(str(block) + ".txt"))['date of birth']
        b_subject = json.load(open(str(block) + ".txt"))['study program']
        b_graduation = json.load(open(str(block) + ".txt"))['date of graduation']

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


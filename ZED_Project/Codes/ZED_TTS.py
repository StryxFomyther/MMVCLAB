# install pyttsx and libgcc
import pyttsx
import time

def obj_pairing(line):
    obj, depth = line.strip().split(',')
    return [obj, float(depth)/100]

def sentence_synth(obj_label, obj_depth, side_margin=0, out_unit='meters'):
    '''
    This function receives the info regarding the closest object in screen
        obj_label -- object label
        obj_depth -- object depth
        side_margin -- optional, states the horizontal location, default 0
        out_unit -- output distance unit, can be meters or feet, default meters
    (Assuming the input distance unit is 'meter'.)
    '''
    obj_label = obj_label
    obj_depth = obj_depth
    
    if out_unit.lower() == 'feet':
        obj_depth *= 3.28084
        side_margin *= 3.28084
    sntnc = 'Closest hazard, a %s, %.1f %s ahead.'%(obj_label, obj_depth, out_unit)

    if side_margin > 0:
        sntnc += (' %.1f %s to your right.'%(side_margin, out_unit))
    elif side_margin < 0:
        sntnc += (' %.1f %s to your left.'%(side_margin, out_unit))
    return sntnc

# sound = engine.getProperty('voices')
# engine.setProperty('voice', sound[16].id)

path = '/home/cheng/Documents/ZED_Project/'
while True:
    with open(path + 'depth.txt') as file_object:
        lines = file_object.readlines()

    obj_dict = dict(map(obj_pairing, lines))
    obj_label, obj_depth = sorted(obj_dict.items(), key=lambda x: x[1])[0]

    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(sentence_synth(obj_label, obj_depth, out_unit='feet'))
    engine.runAndWait()
    engine = None
    time.sleep(5)

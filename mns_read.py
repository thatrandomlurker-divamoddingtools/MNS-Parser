from sys import argv
import struct

internal_count = int(1)

with open(argv[1], 'rb') as infile:
    with open(f'{argv[1][:-3]}csv', 'w') as outfile:
        with open(f'{argv[1][:-4]}_header.csv', 'w') as headerfile:
            outfile.write('beat,half_flag,measure,note_type,hold_duration,type\n')
            signature_MNS = infile.read(3)
            signature_null = infile.read(1)
            Field04_bytes = infile.read(4)
            Field08_bytes = infile.read(4)
            Music_ID_bytes = infile.read(4)
            BPM_bytes = infile.read(4)
            MusID_MA_bytes = infile.read(2)
            MusID_MI_bytes = infile.read(2)
            Field18_bytes = infile.read(4)
            NoteCount_bytes = infile.read(4)
            Field20_bytes = infile.read(4)
            
            Sig = str(signature_MNS)
            Sig_null = struct.unpack('b', signature_null)
            Field04 = struct.unpack('i', Field04_bytes)
            Field08 = struct.unpack('i', Field08_bytes)
            Music_ID = struct.unpack('i', Music_ID_bytes)
            BPM = struct.unpack('f', BPM_bytes)
            MusID_MA = struct.unpack('h', MusID_MA_bytes)
            MusID_MI = struct.unpack('h', MusID_MI_bytes)
            Field18 = struct.unpack('i', Field18_bytes)
            NoteCount = struct.unpack('i', NoteCount_bytes)
            Field20 = struct.unpack('i', Field20_bytes)
            
            headerfile.write(f'{Sig}{Sig_null[0]},{Field04[0]},{Field08[0]},{Music_ID[0]},{BPM[0]},{MusID_MA[0]},{MusID_MI[0]},{Field18[0]},{NoteCount[0]},{Field20[0]}\n')
            
            while True:
                if internal_count > int(NoteCount[0]):
                    break
                    
                beat_high_bytes = infile.read(1)
                beat_low_bytes = infile.read(1)
                measure_bytes = infile.read(2)
                button_bytes = infile.read(1)
                hold_length_bytes = infile.read(1)
                type_bytes = infile.read(2)
                
                beat_high = struct.unpack('b', beat_high_bytes)
                beat_low = struct.unpack('b', beat_low_bytes)
                measure = struct.unpack('h', measure_bytes)
                button_ID = struct.unpack('b', button_bytes)
                hold_length = struct.unpack('b', hold_length_bytes)
                type = struct.unpack('h', type_bytes)
                
                if beat_low[0] == -128:
                    beat_half = int(1)
                else:
                    beat_half = int(0)
                   
                if button_ID[0] == 0:
                    button = 'Down'
                elif button_ID[0] == 1:
                    button = 'Cross'
                elif button_ID[0] == 2:
                    button = 'Left'
                elif button_ID[0] == 3:
                    button = 'Circle'
                elif button_ID[0] == 4:
                    button = 'Up'
                elif button_ID[0] == 5:
                    button = 'Triangle'
                elif button_ID[0] == 8:
                    button = 'Scratch'
                
                outfile.write(f'{beat_high[0]},{beat_half},{measure[0]},{button},{hold_length[0]},{type[0]}\n')
                prev_beat_high = beat_high[0]
                prev_beat_low = beat_low[0]
                prev_measure = measure[0]
                
                internal_count += 1
                            
                        
                        
            
            
        
        
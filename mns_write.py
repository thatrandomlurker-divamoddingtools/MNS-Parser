from sys import argv
import struct

with open(argv[1], 'r') as infile:
    with open(f'{argv[1][:-4]}_header.csv', 'r') as header:
        with open(f'{argv[1][:-3]}bin', 'wb') as output:
            header_line = header.readlines()
            split_header = header_line[1].split(',')
            output.write(b'MNS\x00')
            Field04_Packed = struct.pack('i', int(split_header[1]))
            output.write(Field04_Packed)
            Field08_Packed = struct.pack('i', int(split_header[2]))
            output.write(Field08_Packed)
            MusID_Packed = struct.pack('i', int(split_header[3]))
            output.write(MusID_Packed)
            BPM_Packed = struct.pack('f', float(split_header[4]))
            output.write(BPM_Packed)
            MusIDMa_Packed = struct.pack('h', int(split_header[5]))
            output.write(MusIDMa_Packed)
            MusIDMi_Packed = struct.pack('h', int(split_header[6]))
            output.write(MusIDMi_Packed)
            Field18_Packed = struct.pack('i', int(split_header[7]))
            output.write(Field18_Packed)
            NoteCount_Packed = struct.pack('i', int(split_header[8]))
            output.write(NoteCount_Packed)
            Field20_Packed = struct.pack('i', int(split_header[9]))
            output.write(Field20_Packed)
            
            for line in infile:
                split_note = line.split(',')
                if split_note[0] == 'beat':
                    continue
                
                beat = int(split_note[0])
                half_flag = int(split_note[1])
                measure = int(split_note[2])
                note_name = split_note[3]
                hold_length = int(split_note[4])
                type = int(split_note[5])
                
                if note_name == 'Down':
                    note_id = int(0)
                elif note_name == 'Cross':
                    note_id = int(1)
                elif note_name == 'Left':
                    note_id = int(2)
                elif note_name == 'Circle':
                    note_id = int(3)
                elif note_name == 'Up':
                    note_id = int(4)
                elif note_name == 'Triangle':
                    note_id = int(5)
                elif note_name == 'Scratch':
                    note_id = int(8)
                    
                beat_packed = struct.pack('b', beat)
                output.write(beat_packed)
                if half_flag == 1:
                    output.write(b'\x80')
                elif half_flag == 0:
                    output.write(b'\x00')
                measure_packed = struct.pack('h', measure)
                output.write(measure_packed)
                note_packed = struct.pack('b', note_id)
                output.write(note_packed)
                holdlength_packed = struct.pack('b', hold_length)
                output.write(holdlength_packed)
                type_packed = struct.pack('h', type)
                output.write(type_packed)
                    
            
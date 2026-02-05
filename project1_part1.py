import message_tuple as mt

class AES:
    def __init__(self, key, message):
        self.key = key
        self.message = message
        
    def message_table(self, message):
        table = [[], [], [], []]
        for i in range(0, len(message), 8):
            byte = message[i:i+8]
            row_index = i // 8 % 4
            table[row_index].append(byte)
        return table
    
    def shift_rows(self, table):
        shifted_table = []
        for i in range(4):
            if i == 0:
                shifted_table.append(table[i])
            elif i == 1:
                shifted_table.append(table[i][1:] + table[i][:1])
            elif i == 2:
                shifted_table.append(table[i][2:] + table[i][:2])
            elif i == 3:
                shifted_table.append(table[i][3:] + table[i][:3])
        return shifted_table
    
    def mixColumns(self, state):
        for i in range(4):
            s0 = state[0][i]
            s1 = state[1][i]
            s2 = state[2][i]
            s3 = state[3][i]

            s0 = (self.timesTwo(state[0][i]) ^ self.timesThree(state[1][i]) ^ state[2][i] ^ state[3][i]) & 0xff
            s1 = (state[0][i] ^ self.timesTwo(state[1][i]) ^ self.timesThree(state[2][i]) ^ state[3][i]) & 0xff
            s2 = (state[0][i] ^ state[1][i] ^ self.timesTwo(state[2][i]) ^ self.timesThree(state[3][i])) & 0xff
            s3 = (self.timesThree(state[0][i]) ^ state[1][i] ^ state[2][i] ^ self.timesTwo(state[3][i])) & 0xff

            state[0][i] = s0
            state[1][i] = s1
            state[2][i] = s2
            state[3][i] = s3
            
    def timesTwo(self, byte):
        if byte & 0x80:
            return ((byte << 1) ^ 0x1b) & 0xff
        else:
            return (byte << 1) & 0xff

    def timesThree(self, byte):
        return self.timesTwo(byte) ^ byte
        
    def encrypt(key, message):
        # Placeholder for AES encryption logic
        pass
        

    
   
def main():
    cipher = AES(mt.key, mt.message)
    
    cipher_table = cipher.message_table(cipher.message)
    print("Cipher Table:")
    print(cipher_table)
    shifted_table = cipher.shift_rows(cipher_table)
    print("Shifted Table:")
    print(shifted_table)
    
if __name__ == "__main__":
    main()






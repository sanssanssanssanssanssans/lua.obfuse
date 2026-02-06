class LZSS:
    def __init__(self, window : int = 4095, maxlen : int = 18):
        self.WINDOW = window
        self.MAXLEN = maxlen
    
    def compress(self, data: bytes) -> bytes:
        n = len(data)
        i = 0
        output = bytearray()
        WINDOW = self.WINDOW
        MAXLEN = self.MAXLEN
        while i < n:
            pos = len(output)
            output.append(0)
            value = 0
            items = []
            for _ in range(8):
                if i >= n:
                    break
                start = max(0, i - WINDOW)
                bestl = 0
                besto = 0
                if i - 1 >= start:
                    for j in range(start, i):
                        l = 0
                        while l < MAXLEN and i + l < n and data[j + l] == data[i + l] : l += 1
                        if l > bestl :
                            bestl = l
                            besto = i - j
                            if bestl == MAXLEN:
                                break
                if bestl >= 3:
                    off = besto - 1
                    hi = (off >> 4) & 0xFF
                    lo = ((off & 0xF) << 4) | ((bestl - 3) & 0xF)
                    items += bytes([hi, lo]),
                    i += bestl
                else :
                    items += bytes([data[i]]),
                    i += 1
            idx = 0
            for bit in range(8):
                if idx >= len(items):
                    break
                if len(items[idx]) == 1:
                    value |= (1 << bit)
                idx += 1
            output[pos] = value
            for it in items: output. extend(it)
        return bytes(output)
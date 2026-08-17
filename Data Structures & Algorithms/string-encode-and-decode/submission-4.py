class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            encoded.append(str(len(word)))
            encoded.append(":")
            encoded.append(word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            colon = s.find(":", i)

            if colon == -1:
                raise ValueError("Invalid encoded string")

            length = int(s[i:colon])

            start = colon + 1
            end = start + length

            if end > len(s):
                raise ValueError("Invalid encoded string")

            decoded.append(s[start:end])
            i = end

        return decoded
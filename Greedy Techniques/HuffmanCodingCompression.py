import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        combined_freq = left_node.freq + right_node.freq
        new_node = HuffmanNode(None, combined_freq)
        new_node.left = left_node
        new_node.right = right_node
        heapq.heappush(heap, new_node)

    return heap[0]


def build_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node is not None:
            if node.char:
                codes[node.char] = code
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes


def huffman_compress(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1

    huffman_tree = build_huffman_tree(freq_map)
    huffman_codes = build_huffman_codes(huffman_tree)

    compressed_text = ''.join(huffman_codes[char] for char in text)

    return compressed_text, huffman_codes


def huffman_decompress(compressed_text, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}

    decoded_text = ""
    current_code = ""
    for bit in compressed_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""

    return decoded_text


def main():
    # Example usage
    text = "ABBCCCDDDDEEEEE"

    compressed_text, huffman_codes = huffman_compress(text)
    print("Compressed text:", compressed_text)
    print("Huffman codes:", huffman_codes)

    decoded_text = huffman_decompress(compressed_text, huffman_codes)
    print("Decoded text:", decoded_text)

if __name__ == '__main__':
    main()

def chunk_list(data, size):
    chunks = []
    
    for i in range(0, len(data), size):
        #add and divide the chunk list
        chunks.append(data[i:i+size])
    
    return chunks


numbers = [1,2,3,4,5,6,7,8,9,10]

result = chunk_list(numbers, 3)

print(result)
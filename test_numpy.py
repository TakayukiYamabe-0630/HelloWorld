import numpy as np

def main():
    test2()
    
def test():
    a = np.array([[1,2], [3, 4], [5, 6]])
 
    # ファンシーインデックス参照の例
    # 表示される配列は形状(3,)を持ち、
     
    print(a[[0, 1, 2], [0, 1, 0]]) # "[1 4 5]"と表示
     
    # 上記の例は以下と同様
    print(np.array([a[0, 0], a[1, 1], a[2, 0]])) #"[1 4 5]"と表示
     
    # ファンシーインデックス参照では同じ要素の抽出も可能
    print(a[[0, 0], [1, 1]]) # "[2 2]"と表示
     
    # 上記の例は以下と同様
    print(np.array([a[0, 1], a[0, 1]])) # "[2 2]"と表示
    
def test2():
    # 要素抽出用に新しい配列を作成
 
    a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
     
    print(a) # "[[ 1, 2, 3]
    # [ 4, 5, 6]
    # [ 7, 8, 9]
    # [10, 11, 12]]"と表示
     
    # インデックスの配列を作成
     
    b = np.array([0, 2, 0, 1])
     
    # aからインデックス配列bを使って各行の要素を一つずつ取り出す
     
    print(a[np.arange(4), b]) # Prints "[ 1 6 7 11]"
     
    # aからインデックス配列bを使って各行の要素を一つずつ変更する
     
    a[np.arange(4), b] += 10
     
    print(a) # "[[11, 2, 3]
    # [ 4, 5, 16]
    # [17, 8, 9]
    # [10, 21, 12]]"と表示
    
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
            
if __name__ == '__main__':
    main()
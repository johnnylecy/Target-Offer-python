def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False

        root = sequence[-1]
        length = len(sequence)
        if min(sequence) > root or max(sequence) < root:
            return True
        index = 0
        # 二叉搜索树的左子树结点小于根节点
        '''
        下面这个for循环特别需要主要index=i必须写在if语句外面,
        否则就会发生当root结点前的所有元素小于root的时候, 正确判断应该为True,
        但是因为if语句没有进入, index = 0 ,
        在进入二叉搜索树的右子树结点大于根结点的for循环的时候, 因为sequence的数都小于root, 就会判断出错
        '''
        for i in range(length-1):
            index = i
            if sequence[i] > root:
                break

        # 二叉搜索树的右子树结点大于根结点
        # 这个循环中范围起始点必须是index+1, 不能为index
        # 因为当root结点前的所有元素小于root的时候,index=length-2,
        # 此时sequence[index]<root, 但是按照range(index, length-1), 第一个元素sequence[j]==sequence[index] < root, 返回False, 实际应该返回True才对
        # 而使用index+1, 因为已经默认index>root, 所以从后面一个开始盘算右子树结点是否大于root, 也不会影响结果
        for j in range(index+1, length-1):
            if sequence[j] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])
        return left and right
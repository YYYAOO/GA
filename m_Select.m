function parentPop=m_Select(matrixFitness,pop,SELECTRATE)
%% ѡ��
% ���룺matrixFitness--��Ӧ�Ⱦ���
%      pop--��ʼ��Ⱥ
%      SELECTRATE--ѡ����

sumFitness=sum(matrixFitness(:));%����������Ⱥ����Ӧ��

accP=cumsum(matrixFitness/sumFitness);%�ۻ�����
%cumsum����ͨ�����ڼ���һ��������е��ۼ�ֵ

%���̶�ѡ���㷨
for n=1:round(SELECTRATE*size(pop,2))%size(pop,2)��ʾ����pop������SELECTRATE*size(pop,2)��ʾѡ�����ٸ�
    matrix=find(accP>rand); %�ҵ������������ۻ����ʣ�find�������������еķ���Ԫ�ص�λ��
    if isempty(matrix)
        continue
    end
    parentPop(:,n)=pop(:,matrix(1));%���׸������������ۻ����ʵ�λ�õĸ����Ŵ���ȥ
end
end
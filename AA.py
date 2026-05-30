#utf-8#
#该程序仅能测试您的中英[指缩写]的相互辨识的能力




dz=["甘氨酸","丙氨酸","缬氨酸","亮氨酸","异亮氨酸","脯氨酸","甲硫氨酸","丝氨酸","半胱氨酸","苏氨酸","天冬酰胺","谷氨酰胺","苯丙氨酸","酪氨酸","色氨酸","天冬氨酸","谷氨酸","赖氨酸","精氨酸","组氨酸"]
#创建中文的名称列表
de=["Gly","Ala","Val","Leu","Ile","Pro","Met","Ser","Cys","Thr","Asn","Gln","Phe","Tyr","Trp","Asp","Glu","Arg","Lys","His"]
#创建英文缩写列表
import random#引入随机数函数
p=input("若要出英答中请输入e，若要出中答英请输入z\n")#让用户选择模式
sum,score=0,0#score用于记录正确题数，sum用于记录总题数
qu="1"#这是在后面用于让用户选择是否继续进行用的变量
while p=="z" and qu=="1":
        i=random.randint(0,19)#随机选择一个中文
        print(dz[i])#随机选择一个中文
        u=input("请回答：")#获取回答
        sum=sum+1#记录题数
        if u==de[i]:#判断是否回答正确
            print("才....才不会说你回答正确呢！")
            score=score+1
        else:
            print(f"笨蛋！回答错误。正确答案是:{de[i]}")
        if sum>=10:#当题数大于等于10时，询问是否继续考察
            qu=input("你已回答了十题，若还要继续请输入2,并查看答对题总数，输入3退出")#让用户选择是否退出
            while qu=="2":
                print(f"你回答的题数为{sum},其中正确的题数为{score},正确率为{score/sum:.2%}")#输出总题数，正确题数和正确率
                qu="1"#让程序继续进行
                break
            if qu=="3":#退出程序
                break
            sum,score=0,0#清空记录
while p=="e" and qu=="1":
        i=random.randint(0,19)#随机选择一个英文
        print(de[i])#随机选择一个中文
        u=input("请回答：")#获取回答
        sum=sum+1#记录题数
        if u==dz[i]:#判断是否回答正确
            print("才....才不会说你回答正确呢！")
            score=score+1
        else:
            print(f"笨蛋！回答错误。正确答案是{dz[i]}")
        if sum>=10:#当题数大于等于10时，询问是否继续考察
            qu=input("你已回答了十题，若还要继续请输入2,并查看答对题总数，输入3退出")#让用户选择是否退出
            while qu=="2":
                print(f"你回答的题数为{sum},其中正确的题数为{score},正确率为{score/sum:.2%}")#输出总题数，正确题数和正确率
                qu="1"#让程序继续进行
                break
            if qu=="3":#退出程序
                break
            sum,score=0,0#清空记录
print("感谢您的使用")


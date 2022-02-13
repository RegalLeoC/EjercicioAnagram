# def len_comp(original, anagram):
#     check1 = len(original) - original.count(" ")
#     check2 = len(anagram) - anagram.count(" ")
#     size = (bool(check1 == check2))
#
#     if size is True:
#         l1 = original.replace(" ", "")
#         l2 = anagram.replace(" ", "")
#
#         div1 = list(l1)
#         div2 = list(reversed(l2))
#
#         for i in range(0,len(l1),1):
#
#             if (bool(div1[i] == div2[i])) == True:
#                 cr = True
#             elif (bool(div1[i] == div2[i])) == False:
#                 cr = False
#                 break
#
#         if cr is True:
#             return True
#         elif cr is False:
#             return False
#
#     elif size is False:
#         return False

def len_comp(original, anagram):
    check1 = len(original) - original.count(" ")
    check2 = len(anagram) - anagram.count(" ")
    size = (bool(check1 == check2))

    if size is True:
        l1 = original.replace(" ", "")
        l2 = anagram.replace(" ", "")

        div1 = list(l1)
        div2 = list(l2)

        newdiv1 = div1
        newdiv2 = div2




        for i in range(0,len(div1),1):
            for x in range(0,len(div2),1):
                if (bool(div1[i] == div2[x])) == True:
                    rev = True
                    div2[x] = "_"
                    break

            if rev is False:
                cr = False
                break
            elif rev is True:
                rev = False
                cr = True


        # #Revision del segundo al primero
        # for i in range(0,len(newdiv1)-1,1):
        #     for x in range(0,len(newdiv2)-1,1):
        #         if (bool(newdiv2[i] == newdiv1[x])) == True:
        #             rev = True
        #             newdiv1[x] = "_"
        #             break
        #
        #     if rev is False:
        #         cr = False
        #         break
        #     elif rev is True:
        #         rev = False
        #         cr = True
        # cr = True
        # l = False
        #
        # while cr is True:
        #     for i in range(1, len(div1), 1):
        #         while l is False:
        #             for x in range(1,len(div2),1):
        #                 rev = (bool(div2[i - 1] == div1[x - 1]))
        #                 if rev is True:
        #                     l = True
        #                     div1[x - 1] = "_"
        #             if l is False:
        #                 cr = False
        #                 break
        #         l = False
        #
        #




        if cr is True:
            return True
        elif cr is False:
            return False

    elif size is False:
        return False

# 《放学后的三分钟》
# 短篇校园恋爱 · 双视角（林澈 × 苏晚）
#
# 贯穿意象：书签 + 诗句「把黄昏折进书页里，明天再打开。」


# ---- 角色定义 ----

define narrator = Character(None)
define lc = Character("林澈", color="#5b8def")
define sw = Character("苏晚", color="#ef8fd0")

# 用于居中显示「视角切换」「结局」等提示文字
define ctitle = Character(None, what_xalign=0.5, what_text_align=0.5)


# ---- 状态变量 ----

default affection = 0        # 好感度（0~3）
default bookmark_choice = 0  # 选择①：0=当场还，1=明天还
default library_choice = 0   # 选择②：0=主动帮忙，1=默默离开
default rain_choice = 0      # 选择③：0=送她回家，1=借伞给她
default confessed = False    # 最终是否告白


# ---- 游戏开始 ----

label start:

    # ============ 序幕 ============
    play music "bgm_daily.ogg" fadein 1.0

    scene bg classroom
    with fade

    narrator "放学的铃声，在黄昏的走廊里荡了很久。"

    narrator "教室里的人一个接一个地走了，最后只剩下值日生。"

    narrator "——也就是我，林澈。"

    jump act_one


# ============ 第一幕 · 林澈视角 ============

label act_one:

    scene bg classroom
    with dissolve

    narrator "又轮到我值日了。其实也不算倒霉，我反而有点喜欢这样的安静。"

    narrator "扫地、擦黑板、把椅子一把把翻到桌上。"

    narrator "扫帚碰到靠窗那张桌子的时候，一张纸片从桌角滑了下来，飘到地上。"

    narrator "我蹲下去捡起来。是一张书签。"

    narrator "上面有一行清秀的字迹："

    narrator "「把黄昏折进书页里，明天再打开。」"

    narrator "我认得这个字迹。是苏晚的。"

    narrator "苏晚是我们班的图书委员，坐在靠窗那一排，安静得像一本合上的书。"

    narrator "现在，教室里空荡荡的，她的书签躺在我手里。"

    narrator "也许，她还没走远。"

    menu:
        "追出去，把书签还给她":
            $ bookmark_choice = 0
            jump bookmark_now
        "先收起来，明天再还":
            $ bookmark_choice = 1
            jump bookmark_tomorrow


label bookmark_now:

    scene bg gate
    with dissolve

    narrator "我攥着书签，跑出教室。"

    narrator "在校门口，我看见了她的背影。夕阳把她的影子拉得很长。"

    lc "苏晚！"

    show sw normal at center
    with dissolve

    sw "……林澈？"

    lc "你的书签掉了。"

    narrator "我把书签递过去。她的眼睛微微睁大了一点。"

    sw "啊……谢谢。"

    narrator "她接过书签，指尖轻轻擦过我的手心。"

    sw "你……看到上面的字了？"

    lc "嗯。写得真好。"

    show sw shy at center
    with dissolve

    sw "……谢谢。"

    narrator "她低下头，耳尖有一点点红。不知道为什么，我突然觉得，值日也没那么无聊了。"

    $ affection += 1

    jump act_one_middle


label bookmark_tomorrow:

    scene bg classroom
    with dissolve

    narrator "我把书签小心地夹进自己的课本里。"

    narrator "「明天再还给她吧。」我这么想。其实，是我想多留它一个晚上。"

    scene bg classroom_day
    with dissolve

    narrator "第二天，趁着课间，我走到苏晚的座位前。"

    lc "苏晚，这个……是你的吧？"

    show sw normal at center
    with dissolve

    sw "……啊！我还以为弄丢了。"

    narrator "她把书签接过去，看了很久，然后抬起头。"

    sw "谢谢你帮我收着。"

    sw "上面的字……你看到了？"

    lc "嗯。是你自己写的？"

    show sw smile at center
    with dissolve

    sw "嗯。"

    narrator "她点了点头，眼睛亮了一下。那是我第一次看见她笑。"

    jump act_one_middle


label act_one_middle:

    scene bg library
    with dissolve

    narrator "几天后。"

    narrator "我去图书馆找一本参考书，却在书架之间，看见了苏晚。"

    narrator "她站在一架梯子上，怀里抱着一摞书，摇摇晃晃的。"

    narrator "我犹豫了一下。"

    menu:
        "走过去帮她":
            $ library_choice = 0
            jump library_help
        "假装没看见，默默离开":
            $ library_choice = 1
            jump library_leave


label library_help:

    show sw normal at center
    with dissolve

    lc "我来帮你吧。"

    narrator "我走过去，接过她怀里的书。"

    sw "林澈？谢谢你……你怎么会在这里？"

    lc "来找本书，正好看见你。"

    narrator "我把书一本一本放回高处的架子上。她站在一旁，仰头看着我。"

    show sw smile at center
    with dissolve

    sw "那，作为谢礼——你要找什么书？我帮你找。"

    narrator "那天下午，我们在图书馆里待了很久。她帮我找到了书，还多借了一本给我。"

    $ affection += 1

    jump act_one_end


label library_leave:

    narrator "我停下脚步，又退了回去。"

    narrator "「还是算了。」我对自己说，「她看起来不需要帮忙。」"

    narrator "我转身走了，没有回头。"

    narrator "（我没有看见，她其实早就看见了我。她一直在等我开口。）"

    jump act_one_end


label act_one_end:

    play music "bgm_rain.ogg" fadein 1.0

    scene bg rain_gate
    with dissolve

    narrator "又过了几天。"

    narrator "放学的时候，天突然下起了大雨。"

    narrator "我撑着伞走到校门口，看见苏晚站在屋檐下，望着灰蒙蒙的天。"

    narrator "她没带伞。"

    menu:
        "走上前，说送她回家":
            $ rain_choice = 0
            jump rain_walk
        "把伞塞给她，自己跑进雨里":
            $ rain_choice = 1
            jump rain_lend


label rain_walk:

    show sw normal at center
    with dissolve

    lc "一起走吧。顺路。"

    sw "会、会不会太麻烦你？"

    lc "不会。"

    narrator "于是，我们共撑着一把伞，走进了雨里。"

    narrator "雨点打在伞面上，哒哒地响。我把伞往她那边偏了偏，自己的左肩很快就被淋湿了。"

    show sw shy at center
    with dissolve

    sw "你的肩膀……"

    lc "没事。"

    narrator "她走得很慢，像是在数我们的步子。"

    sw "……谢谢你。"

    $ affection += 1

    jump act_two


label rain_lend:

    narrator "我把伞塞进她手里。"

    lc "你撑着。我家很近，跑两步就到。"

    narrator "说完，我跑进了雨里。"

    sw "等、等一下——"

    narrator "我没有回头。"

    narrator "（我没有看见，她站在屋檐下，望着我跑远的背影，把伞柄握得很紧。）"

    jump act_two


# ============ 第二幕 · 苏晚视角 ============

label act_two:

    play music "bgm_su.ogg" fadein 1.0

    scene black
    with fade

    narrator "……"

    narrator "我撒谎了。"

    narrator "从很久以前，我就一直在看他。"

    scene bg library
    with fade

    ctitle "—— 苏晚视角 ——"

    narrator "我叫苏晚。图书委员，坐在靠窗那一排，安静得像一本合上的书。"

    narrator "他大概不知道，那些「偶遇」，大多不是偶然。"

    if bookmark_choice == 0:

        narrator "那张书签，是我故意放在桌上的。"

        narrator "因为我知道，那天是他值日。我想看看，他会不会注意到我的字。"

        narrator "他追出来的时候，我的心跳得厉害。原来，他看到了。"

        narrator "「写得真好。」他这么说。我差点没能把「谢谢」说清楚。"

    else:

        narrator "那张书签，其实是我故意放在桌上的。"

        narrator "因为我知道，那天是他值日。我想看看，他会不会注意到我的字。"

        narrator "可他一直没有还我。我以为，它丢了。"

        narrator "直到第二天，他把书签还回来，说「这个是你的吧」。"

        narrator "原来，他帮我收着。原来，他也记得。"

    if library_choice == 0:

        narrator "图书馆那次，我是故意抱多了书的。"

        narrator "我站在梯子上，心里一直默念：如果他能过来帮我就好了。"

        narrator "他真的过来了。那一刻，我连呼吸都忘了。"

    else:

        narrator "图书馆那次，我是故意抱多了书的。"

        narrator "我看见他站在书架后面，又看见他转身走了。"

        narrator "我抱着一摞书，站在那里，很久很久。"

    if rain_choice == 0:

        narrator "那天的大雨，我其实带了伞。"

        narrator "我把伞藏在书包里，没有拿出来。因为我在等。"

        narrator "等他走过来，等他问「要不要一起走」。"

        narrator "他真的那么做了。伞很小，我们的肩膀靠得很近。"

        narrator "他的左肩淋湿了，我全都知道。"

    else:

        narrator "那天的大雨，我其实带了伞。"

        narrator "我把伞藏在书包里，没有拿出来。因为我在等。"

        narrator "可是，他把伞塞给我，自己跑进了雨里。"

        narrator "我喊他，他没有回头。"

        narrator "我撑着那把伞，站在原地。伞柄上，还留着他手心的温度。"

    narrator "我一直在想，这些到底算不算「喜欢」。"

    narrator "后来我知道了。喜欢一个人，就是会想尽办法，制造一次「偶然」。"

    jump act_three


# ============ 第三幕 · 交汇 ============

label act_three:

    play music "bgm_confess.ogg" fadein 1.0

    scene bg rooftop
    with fade

    narrator "学园祭的最后一天，黄昏。"

    narrator "天台上，只剩下我们两个人。风把横幅吹得哗哗响。"

    show sw normal at center
    with dissolve

    sw "林澈。"

    lc "苏晚。"

    narrator "我们几乎同时开口，又同时停下。"

    narrator "沉默了一会儿。她低头，又抬头，像下定了什么决心。"

    narrator "我知道，有些话，现在不说，就再也没机会了。"

    menu:
        "「我有一句话，一直想对你说。」":
            $ confessed = True
            jump final_confess
        "（什么都说不出口。）":
            $ confessed = False
            jump final_silence


label final_confess:

    lc "苏晚，我……喜欢你。"

    lc "从捡到那张书签开始，就喜欢你了。"

    if affection >= 2:
        jump ending_good
    else:
        jump ending_normal


label final_silence:

    narrator "可是，话到嘴边，却怎么也说不出口。"

    narrator "我低下了头。"

    if affection >= 2:
        jump ending_normal
    else:
        jump ending_miss


# ============ 结局 ============

label ending_good:

    show sw smile at center
    with dissolve

    sw "……我也是。"

    sw "从很久以前，就一直是。"

    narrator "她笑了，眼角有泪光。晚霞把天台的每一个角落都染成了橘红色。"

    sw "这个，送给你。"

    narrator "她递过来一样东西。是那张书签。"

    narrator "只是，在原来那行字下面，又多了一行："

    narrator "「明天，我陪你一起打开。」"

    scene black
    with fade

    ctitle "—— 好结局 · 黄昏的书签 ——"

    return


label ending_normal:

    play music "bgm_sad.ogg" fadein 1.0

    sw "……嗯。"

    narrator "她低下头，声音轻得像风。"

    sw "那……谢谢你，一直以来的照顾。"

    narrator "我站在原地，看着她转身离开。夕阳把她的影子拉得很长，和那天一样。"

    narrator "有些话，终究还是迟了一点。"

    scene black
    with fade

    ctitle "—— 普通结局 · 借来的伞 ——"

    return


label ending_miss:

    play music "bgm_sad.ogg" fadein 1.0

    narrator "我们就那样，谁也没有再说话。"

    narrator "天黑了。学园祭的灯一盏一盏灭掉。"

    narrator "再后来，毕业，各奔东西。"

    narrator "那张书签，始终夹在我的课本里，再也没有还回去。"

    narrator "「把黄昏折进书页里，明天再打开。」"

    narrator "而明天，已经不会再来了。"

    scene black
    with fade

    ctitle "—— 错过结局 · 空教室 ——"

    return

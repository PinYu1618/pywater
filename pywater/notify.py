import random

from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler

TITLE = "Time to drink water!"


def setup_notify():
    # setup notification background scheduler
    sched = BackgroundScheduler(timezone="Asia/Taipei")
    sched.add_job(_notify, "interval", seconds=5)  # change this to hour in dist
    sched.start()
    print("Schedule started...")


def _notify():
    notification.notify(
        title=TITLE, message=_encourage(), app_icon=None, timeout=3, toast=False
    )


# 鼓勵話語
def _encourage():
    encouraging_phrases = [
        "健康是最好的禮物，每一個健康的日子都是一份無價的珍寶。",
        "要想享受生活的美好，首先要照顧好自己的身體，健康是幸福的基石。",
        "不要等到身體出現問題才開始注意健康，預防勝於治療。",
        "健康不僅是身體的良好狀態，也是心靈和情緒的平衡。",
        "小小的健康習慣，長遠的幸福生活，每一個良好的選擇都是對自己的愛。",
        "健康不是目的地，而是一生的旅程，每一步都是對自己的投資。",
        "每天給自己一點運動，一點均衡的飲食，是對未來最好的投資。",
        "保持正向的心態，笑容是最好的良藥，讓快樂成為你的健康習慣。",
        "當你感到疲憊時，不要放棄，這是成長的一部分，堅持下去，你會更強大。",
        "健康是人生的第一財富，好的身體是實現夢想的基石，讓健康陪伴你走向美好的未來。",
        "擁有健康的身體就是擁有無窮的可能性，讓自己成為生活的勇者。",
        "每一個燃燒的卡路里都是對自己的關愛，運動是身體最美好的語言。",
        "飲食是生命的能量，選擇健康食材就是選擇給自己更好的生活。",
        "好的休息是健康的基礎，讓自己有足夠的睡眠是對自己的最大呵護。",
        "活出精彩的人生，從尊重自己的身體開始，給自己最好的照顧。",
        "健康是生活的動力，給自己一個強健的身體，就是給自己一個幸福的未來。",
        "每一次汗水的流淌都是對自己的付出，堅持運動是對生命的敬意。",
        "健康不僅是外在的美，更是內在的健康與活力，讓自己散發出光彩。",
        "養成健康的生活習慣，就是給自己最好的禮物，是對自己的一份美好承諾。",
        "在生活的旅途中，保護好自己的身體，讓自己的心靈飛翔。",
    ]
    n = random.randint(0, 19)
    return encouraging_phrases[n]

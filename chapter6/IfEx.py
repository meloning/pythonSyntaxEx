signal_color = input('색을 영문을 입력하세요: ')

if signal_color == 'blue':
    print('신호등은 파란색입니다. 건너세요')

    is_pass = input('건널 준비가 되었나요? (yes/no)')
    if is_pass == 'yes':
        print('건너')
    else:
        print('담에 건너')

elif signal_color == 'red':
    print('신호등은 빨간색입니다. 기다리세요')
else:
    print('잘못된 색입니다.')
import sys
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien
from time import sleep

def check_play_button(setting , screen , stats , play_button , ship , aliens , bullets , mouse_x , mouse_y):
	"""在玩家单击play按钮时开始新游戏"""
	if play_button.rect.collidepoint(mouse_x , mouse_y) and not stats.game_active:
		# 隐藏光标
		pygame.mouse.set_visible(False)
		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		#清空外星人和子弹列表
		aliens.empty()
		bullets.empty()
		
		#创建一群新的外星人，并让飞船居中
		create_fleet(setting , screen , ship , aliens)
		ship.center_ship()
		setting.initialize_dynamic_setting()

def check_game_over(stats , setting, aliens , ship ,screen , bullets):
	if pygame.sprite.spritecollideany(ship , aliens) or check_aliens_bottom(aliens , screen ,setting):
		ship_hit(setting , stats , screen , ship , aliens , bullets)

def check_aliens_bottom(aliens , screen ,setting):
	for alien in aliens:
		if alien.rect.bottom >= setting.screen_height:
			return True
	return False
		
def ship_hit(setting , stats , screen , ship , aliens , bullets):
	if stats.ships_left > 0:
		stats.ships_left -= 1
	
		aliens.empty()
		bullets.empty()
	
		create_fleet(setting , screen , ship , aliens)
		ship.center_ship()
	
		sleep(0.5)
	else :
		stats.game_active = False
		pygame.mouse.set_visible(True)

	
def delet_alien(aliens, bullets , setting , screen , ship ):
	"""删除现有的子弹， 加快游戏节奏 ， 并创建一群新的外星人"""
	collisions = pygame.sprite.groupcollide(bullets , aliens , True ,True)
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(setting , screen , ship , aliens)
		#加快游戏节奏
		setting.increase_speed()

def update_aliens(setting , aliens):
	check_fleet_edges(setting , aliens)
	aliens.update()

def check_fleet_edges(setting , aliens):
	"""检查外星人是否到达了屏幕边缘 如果到达就更改方向"""
	for alien in aliens:
		if alien.check_edges():
			change_fleet_direction(setting , aliens)
			break
	
def change_fleet_direction(setting , aliens):
	"""检查是否有外星人位于屏幕边缘 ， 并更新整群外星人的位置"""
	for alien in aliens.sprites():
		alien.rect.y += setting.alien_speed_factor_y
	setting.fleet_direction *= -1

def create_fleet(setting , screen , ship , aliens):
	alien = Alien(setting , screen)
	alien_width  = alien.rect.width
	
	number_alien_x = get_alien_num(alien_width , setting)
	# 获得外星人的行数
	number_rows = get_number_rows(setting , ship.rect.height , alien.rect.height)
	for row_number in range(number_rows):
		for alien_num in range(number_alien_x):
			create_alien(setting , screen , aliens , alien_num , alien_width , row_number)

def create_alien(setting , screen , aliens , alien_num , alien_width  , row_number):
	alien = Alien(setting , screen)
	alien.x = alien_width + 2 * alien_width * alien_num
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def get_alien_num(alien_width , setting):
	avaliable_space_x = setting.screen_width - 2 * alien_width
	number_alien_x = int(avaliable_space_x /(2 * alien_width))
	return number_alien_x

def get_number_rows(setting , ship_height , alien_height):
	avaliable_space_y = setting.screen_height - 3 * alien_height - ship_height
	number_rows = avaliable_space_y // (2 * alien_height)
	return number_rows
	
def check_events(ship, bullets, screen, setting ,stats , play_button , aliens ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, screen, setting)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_button(setting , screen , stats , play_button , ship , aliens , bullets , mouse_x , mouse_y)


def update_screen(screen, ship, setting, bullets , aliens , play_button ,stats):
    # 重绘屏幕
    screen.fill(setting.bg_color)
    ship.blitme()
	#绘制外星人
    for alien in aliens:
        alien.blitme()
	
	#绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
	
	#如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def del_bullet(bullets):
    """删除溢出屏幕的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_keydown_events(event, ship, bullets, screen, setting):
    """检查键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and len(bullets) <= setting.bullet_allowed:  # 创建新的子弹
        bullets.add(Bullet(setting, screen, ship))

def check_keyup_events(event, ship):
    """检查按键抬起事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

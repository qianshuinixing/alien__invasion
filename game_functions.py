import sys
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien

def create_fleet(setting , screen , aliens):
	alien = Alien(setting , screen)
	alien_width  = alien.rect.width
	
	number_alien_x = get_alien_num(alien_width , setting)
	for alien_num in range(number_alien_x):
		create_alien(setting , screen , aliens , alien_num , alien_width)

def create_alien(setting , screen , aliens , alien_num , alien_width):
	alien = Alien(setting , screen)
	alien.x = alien_width + 2 * alien_width * alien_num
	alien.rect.x = alien.x
	aliens.add(alien)
	
def get_alien_num(alien_width , setting):
	avaliable_space_x = setting.screen_width - 2 * alien_width
	number_alien_x = int(avaliable_space_x /(2 * alien_width))
	return number_alien_x
		
def check_events(ship, bullets, screen, setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, screen, setting)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, ship, setting, bullets , aliens):
    # 重绘屏幕
    screen.fill(setting.bg_color)
    ship.blitme()
	#绘制外星人
    for alien in aliens:
        alien.blitme()
	
	#绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()

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

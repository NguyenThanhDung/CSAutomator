import time
from Defines import GameState, ShoesSource, DailyMission
from Screen import ScreenType
from ButtonPositions import ButtonPositions, Button, Position
from Equipment import Equipment
from MagicShop import MagicShop
from Profile import Profile, ProfileField

class GameManager:

    def __init__(self, device, profile):
        self.device = device
        self.profile = profile
        self.screen = None
        self.gameState = GameState.PROMOTION_BATTLE
        self.shoesSource = ShoesSource.DAILY_MISSION_REWARD
        self.dailMissionState = DailyMission.NONE
        self.scrollStep = 0
        self.purchaseConfirmed = False
        self.magicShop = MagicShop()

    def SetScreen(self, screen):
        self.screen = screen

    def Play(self):
        if self.screen.screenType == ScreenType.DEVICE_HOME:
            iconLocation = self.screen.Find("DeviceHome.png", 30000)
            if iconLocation is not None:
                self.Log("Start game")
                self.device.Touch(iconLocation.x + 5, iconLocation.y + 5)
                time.sleep(5)
                self.device.LoadDeviceInfo()
            else:
                self.Log("Can not find the game icon!")
        elif self.screen.screenType == ScreenType.TAP_TO_START:
            self.Log("Tap to start...")
            self.device.Touch(640, 360)
        elif self.screen.screenType == ScreenType.EVENT_INFO_1    \
            or self.screen.screenType == ScreenType.EVENT_INFO_2:
            self.Log("Close event information dialog")
            self.device.Touch(1215, 630)
        elif self.screen.screenType == ScreenType.DIALOG_WEEKLY_LIMITED    \
            or self.screen.screenType == ScreenType.DIALOG_LIMITED_OFFER:
            self.Log("Close dialog")
            self.device.Touch(344, 38)
        elif self.screen.screenType == ScreenType.DIALOG_SUGGESTED_ITEM:
            self.Log("Close dialog")
            self.device.Touch(960, 448)
        elif self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            self.Log("Close dayly log-gin reward")
            self.device.Touch(974, 357)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_DISABLED:
            self.Log("Enable auto play")
            self.device.Touch(58, 107)
        elif self.screen.screenType == ScreenType.REWARD_INFO:
            self.Log("Press OK")
            self.device.Touch(797, 356)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION:
            self.Log("Confirm refresh")
            self.device.Touch(784, 243)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE:
            self.Log("Don't refresh with moonstone")
            self.device.Touch(784, 474)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT_WIN \
            or self.screen.screenType == ScreenType.BATTLE_RESULT_LOSE:
            self.Log("Press Exit")
            self.device.Touch(1196, 115)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            self.Log("Press Skip")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_REFRESH_RESET:
            self.Log("OK")
            self.device.Touch(784, 357)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_TICKETS:
            self.Log("Go to Mysterious Sanctuary...")
            self.gameState = GameState.MYSTERIOUS_SANCTUARY
            self.device.Touch(788, 471)
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DIALOG_PURCHASE_COMPLETE:
            self.Log("Close dialog. Go to battle...")
            self.gameState = GameState.PROMOTION_BATTLE
            self.shoesSource = ShoesSource.DAILY_MISSION_REWARD
            self.device.Touch(783, 355)
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.BATTLE_NEW_SEASON:
            self.Log("OK")
            self.device.Touch(784, 358)
        elif self.screen.screenType == ScreenType.MAIL_BOX_COLLECT:
            self.Log("OK")
            self.device.Touch(799, 357)
        elif self.screen.screenType == ScreenType.DIALOG_UNSTABLE_NETWORK:
            self.Log("Yes")
            self.device.Touch(788, 244)
        elif self.screen.screenType == ScreenType.GAME_HOME:
            screenPiece = self.screen.Find("GameHome_ShopAvailable.png")
            if screenPiece is not None:
                self.Log("Shop available. Go for shoping...")
                self.gameState = GameState.SHOPPING
            else:
                screenPiece = self.screen.Find("GameHome_SummonAvailable.png")
                if screenPiece is not None:
                    self.Log("Summon available. Go to summon...")
                    self.gameState = GameState.SUMMON
                elif self.profile.DidPlayEventDungeonToday() == False   \
                    and self.gameState != GameState.OUT_OF_SHOES:
                    screenPiece = self.screen.Find("GameHome_EventDungeon.png")
                    if screenPiece is not None:
                        self.Log("Event Dungeon available. Go to dungeon...")
                        self.gameState = GameState.EVENT_DUNGEON
                    else:
                        self.Log("Can't find Event Dungeon button. Continue...")
                        self.profile.SaveLastDatePlayEventDungeon()
            self.PlaySubstate()
        else:
            self.PlaySubstate()

    def PlaySubstate(self):
        if self.gameState == GameState.DAILY_MISSION:
            self.PlayDailyMission()
        elif self.gameState == GameState.PROMOTION_BATTLE:
            self.PlayPromotionBattle()
        elif self.gameState == GameState.MYSTERIOUS_SANCTUARY:
            self.PlayMysteriousSanctuary()
        elif self.gameState == GameState.OUT_OF_SHOES:
            self.FindShoes()
        elif self.gameState == GameState.SHOPPING:
            self.Shopping()
        elif self.gameState == GameState.SUMMON:
            self.Summon()
        elif self.gameState == GameState.EVENT_DUNGEON:
            self.PlayEventDungeon()
        else:
            self.PlayDefault()

    def PlayDailyMission(self):
        if self.dailMissionState == DailyMission.NONE:
            if self.screen.screenType == ScreenType.GAME_HOME:
                self.Log("Open daily mission reward")
                self.device.Touch(1184, 634)
                time.sleep(1)
                self.device.Touch(756, 82)
                self.scrollStep = 0
            elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
                self.Log("Idle in 20 seconds...")
                time.sleep(20)
            elif self.screen.screenType == ScreenType.DAILY_MISSION:
                mission = self.screen.Find("DailyMission_Disassembly.png")
                if mission is not None:
                    self.Log("Open mission")
                    self.dailMissionState = DailyMission.DISASSEMBLY
                    self.device.Touch(mission.x + 64, mission.y + 240)
                    return
                mission = self.screen.Find("DailyMission_DearFriend.png")
                if mission is not None:
                    self.dailMissionState = DailyMission.DEAR_FRIEND
                    self.PlayDefault()
                    return
            elif self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB:
                self.Log("Close mail box")
                self.device.Touch(51, 40)
            else:
                self.PlayDefault()
        elif self.dailMissionState == DailyMission.DISASSEMBLY:
            if self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
                self.Log("Go to play mission...")
                self.device.Touch(785, 460)
            else:
                self.PlayDefault()
        elif self.dailMissionState == DailyMission.DEAR_FRIEND:
            if self.screen.screenType == ScreenType.GAME_HOME:
                self.Log("Open Community")
                self.device.Touch(1183, 634)
                time.sleep(1)
                self.device.Touch(891, 632)
            else:
                self.PlayDefault()
        else:
            self.PlayDefault()
    
    def PlayPromotionBattle(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            self.Log("Open map")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            self.Log("Open Promotion Battle")
            self.device.Touch(1077, 547)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            self.Log("Auto place and start")
            self.device.Touch(767, 627)
            time.sleep(1)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            self.Log("Idle in 20 seconds...")
            time.sleep(20)
        elif self.screen.screenType == ScreenType.BATTLE_LIST:
            if self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png") is not None:
                self.Log("Rival available. Switch to Rival list")
                self.device.Touch(1221, 505)
            else:
                potentialMatch = self.screen.Find("PromotionBattle_BattleList_PotentialMatch.png")
                if potentialMatch is not None:
                    self.Log("There is a potential match, go for battle")
                    self.scrollStep = 0
                    self.device.Touch(potentialMatch.x + 40, potentialMatch.y + 70)
                else:
                    if self.scrollStep < 2:
                        self.Log("Can not find any potential match, scroll up")
                        self.device.Swipe(1016, 226, 614, 226)
                        self.scrollStep = self.scrollStep + 1
                    else:
                        self.scrollStep = 0
                        refreshAvailable = self.screen.Find("PromotionBattle_BattleList_RefreshAvailable.png")
                        if refreshAvailable is not None:
                            self.Log("There isn't any potential match, refresh list")
                            self.device.Swipe(569, 226, 1116, 226)
                            self.device.Swipe(569, 226, 1116, 226)
                            self.device.Touch(514, 108)
                        else:
                            self.Log("There isn't any potential match, refresh is not available, go to Mysterious Sanctuary")
                            self.gameState = GameState.MYSTERIOUS_SANCTUARY
        elif self.screen.screenType == ScreenType.RIVAL_LIST:
            rivalAvailable = self.screen.Find("PromotionBattle_RivalList_Available.png")
            if rivalAvailable is not None:
                self.Log("Start Rival match...")
                batteButtonLocaltion = self.screen.Find("PromotionBattle_RivalList_BattleButton.png")
                if batteButtonLocaltion is not None:
                    self.Log("Press Battle button at " + str(batteButtonLocaltion))
                    self.device.Touch(batteButtonLocaltion.x + 5, batteButtonLocaltion.y + 5)
                else:
                    self.Log("Schroll down")
                    self.device.Swipe(1116, 351, 569, 351)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    self.Log("Switch to Battle tab")
                    self.device.Touch(battleAvailable.x + 52, battleAvailable.y + 44)
                else:
                    self.Log("Go home")
                    self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_RANKING:
            rivalAvailable = self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png")
            if rivalAvailable is not None:
                self.Log("Switch to Rival tab")
                self.device.Touch(rivalAvailable.x + 62, rivalAvailable.y + 66)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    self.Log("Switch to Battle tab")
                    self.device.Touch(battleAvailable.x + 52, battleAvailable.y + 44)
                else:
                    self.Log("Play Mysterious Sanctuary...")
                    self.gameState = GameState.MYSTERIOUS_SANCTUARY
                    self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_DEFENSE_RECORD:
            rivalAvailable = self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png")
            if rivalAvailable is not None:
                self.Log("Switch to Rival tab")
                self.device.Touch(rivalAvailable.x + 62, rivalAvailable.y + 66)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    self.Log("Switch to Battle tab")
                    self.device.Touch(battleAvailable.x + 52, battleAvailable.y + 44)
                else:
                    self.Log("Go home")
                    self.device.Touch(38, 46)
        else:
            self.PlayDefault()
    
    def PlayMysteriousSanctuary(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            self.Log("Open map")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            self.Log("Open Mysterious Sanctuary")
            self.device.Touch(630, 600)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            screenPiece = self.screen.Find("MysteriousSanctuary_MapClosed.png", 100000)
            if screenPiece is not None:
                self.Log("Open Shrine of Light")
                self.device.Touch(400, 560)
            else:
                screenPiece = self.screen.Find("ShrineOfLight.png", 100000)
                if screenPiece is not None:
                    self.Log("Swipe up to find 8F")
                    self.device.Swipe(1120, 360, 577, 360)
                else:
                    screenPiece = self.screen.Find("ShrineOfLight_8F.png", 1000000)
                    if screenPiece is not None:
                        self.Log("Open floor 8F")
                        self.device.Touch(screenPiece.x + 54, screenPiece.y + 81)
                    else:
                        self.PlayDefault()
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            screenPiece = self.screen.Find("GuardianPlacement_AutoPlayIsEnabled.png")
            if screenPiece is not None:
                self.Log("Auto Play is enabled. Disable it")
                self.device.Touch(screenPiece.x + 10, screenPiece.y + 10)
            self.Log("Auto place and start")
            self.device.Touch(767, 627)
            time.sleep(1)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            self.Log("Idle in 20 seconds...")
            time.sleep(20)
            # self.Log("Auto touch...")
            # self.AutoTouch(10)
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            self.Log("Replay")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Result_Replay))
        else:
            self.PlayDefault()

    def FindShoes(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            if self.shoesSource == ShoesSource.DAILY_MISSION_REWARD:
                self.Log("Open daily mission reward")
                self.device.Touch(1184, 634)
                time.sleep(1)
                self.device.Touch(756, 82)
                self.scrollStep = 0
            elif self.shoesSource == ShoesSource.MAIL_BOX:
                self.Log("Open mail box")
                self.device.Touch(137, 52)
            elif self.shoesSource == ShoesSource.SHOP_WITH_FP:
                self.Log("Open shop")
                self.device.Touch(1193, 224)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            self.Log("Idle in 20 seconds...")
            time.sleep(20)
        elif self.screen.screenType == ScreenType.DAILY_MISSION:
            collectButton = self.screen.Find("DailyChallenge_CollectButton.png")
            if collectButton is not None:
                self.Log("Collect reward")
                self.device.Touch(collectButton.x + 34, collectButton.y + 66)
            else:
                if self.scrollStep < 2:
                    self.Log("Can not find any reward, scroll up")
                    self.device.Swipe(1158, 273, 265, 273)
                    self.scrollStep = self.scrollStep + 1
                else:
                    self.Log("Collected all rewards, go to battle...")
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.shoesSource = ShoesSource.MAIL_BOX
                    self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
            self.Log("Close pop up")
            self.device.Touch(436, 103)
        elif self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB:
            screenPiece = self.screen.Find("MailBox_CollectButton.png", 100000)
            if screenPiece is not None:
                self.Log("Collect reward")
                self.device.Touch(screenPiece.x + 10, screenPiece.y + 10)
            else:
                self.Log("Mail box is empty. Close mail box, go to shop...")
                self.gameState = GameState.PROMOTION_BATTLE
                self.shoesSource = ShoesSource.SHOP_WITH_FP
                self.device.Touch(51, 40)
        elif self.screen.screenType == ScreenType.SHOP:
            if self.shoesSource == ShoesSource.SHOP_WITH_FP:
                self.Log("Buy shoes with FP")
                # self.device.Swipe(924, 118, 924, 591)
                # time.sleep(1)
                self.device.Touch(1063, 133)
            elif self.shoesSource == ShoesSource.SHOP_WITH_MOONSTONE:
                self.Log("Buy shoes with moonstones")
                self.device.Swipe(924, 591, 924, 118)
                time.sleep(1)
                self.device.Touch(1063, 358)
            else:
                self.Log("Go home")
                self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DIALOG_SHOES_RECHARGE_FP:
            if self.shoesSource == ShoesSource.SHOP_WITH_FP:
                self.Log("Confirm buy shoes with FP")
                self.device.Touch(735, 237)
            else:
                self.Log("Cancel")
                self.device.Touch(735, 477)
        elif self.screen.screenType == ScreenType.DIALOG_SHOES_RECHARGE_II:
            if self.shoesSource == ShoesSource.SHOP_WITH_MOONSTONE:
                self.Log("Confirm buy shoes with moonstones")
                self.device.Touch(735, 237)
            else:
                self.Log("Cancel")
                self.device.Touch(735, 477)
        elif self.screen.screenType == ScreenType.DIALOG_NOT_ENOUGH_FP:
            self.Log("Close dialog. Go to buy shoes by moonstones...")
            self.shoesSource = ShoesSource.DAILY_MISSION_REWARD
            self.device.Touch(785, 357)
        else:
            self.PlayDefault()

    def Shopping(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            self.Log("Press Shop button")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Home_Shop))
        elif self.screen.screenType == ScreenType.SHOP:
            screenPiece = self.screen.Find("Shop_MagicShopAvailable.png")
            if screenPiece is not None:
                self.Log("Magic shop is available. Open magic shop...")
                self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Shop_MagicShop))
            else:
                screenPiece = self.screen.Find("Shop_MagicShopOpening.png")
                if screenPiece is not None:
                    self.Log("Magic shop is opening. Find good items...")
                    self.BuyGoodItemInMagicShop()
                else:
                    self.Log("Magic Shop isn't available. Go home...")
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.PlayDefault()
        elif self.screen.screenType == ScreenType.SHOP_DIALOG_IS_OPENNING:
            screenPiece = self.screen.Find("Shop_DialogIsOpening_MysticalBook.png")
            if screenPiece is not None:
                self.Log("Buy mystical book")
                self.purchaseConfirmed = True
                self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_Purchase))
            else:
                equipment = Equipment(self.screen)
                if equipment.isGood:
                    self.Log("Good equipment. Buy!")
                    self.purchaseConfirmed = True
                    self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_Purchase))
                else:
                    self.Log("Not good equipment. Close")
                    self.purchaseConfirmed = False
                    self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_Cancel))
        elif self.screen.screenType == ScreenType.SHOP_DIALOG_PURCHASE_CONFIRMATION:
            if self.purchaseConfirmed:
                self.Log("Confirm")
                self.purchaseConfirmed = False
                self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_PurchaseConfirmation_OK))
            else:
                self.Log("Cancel")
                self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_PurchaseConfirmation_Cancel))
        else:
            self.PlayDefault()

    def BuyGoodItemInMagicShop(self):
        screenPiece = self.FindGoodItemInMagicShop()
        if screenPiece is not None:
            self.Log("Open item info")
            self.device.Touch(screenPiece.x + 193, screenPiece.y + 70)
            self.magicShop.AddOpenedEquipment(screenPiece)
        else:
            self.magicShop.ClearOpenedEquipments()
            if self.scrollStep < 2:
                self.Log("No good item is found. Find more...")
                self.device.Swipe(989, 127, 989, 594)
                self.scrollStep = self.scrollStep + 1
            else:
                self.Log("No good item is found")
                self.scrollStep = 0
                self.gameState = GameState.PROMOTION_BATTLE
                self.PlayDefault()

    def FindGoodItemInMagicShop(self):
        screenPiece = self.screen.Find("Shop_Equipment_Weapon_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple weapon")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Shield_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple shield")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Armor_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple armor")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Gloves_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple gloves")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Necklace_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple necklace")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Ring_5stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars purple ring")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Weapon_5stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars gold weapon")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Shield_5stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars gold shield")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Armor_5stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars gold armor")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Necklace_5stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars gold necklace")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Ring_5stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 5 stars gold ring")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Weapon_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple weapon")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Shield_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple shield")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Armor_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple armor")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Gloves_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple gloves")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Necklace_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple necklace")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Ring_6stars_Purple.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars purple ring")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Weapon_6stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars gold weapon")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Shield_6stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars gold gloves")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Gloves_6stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars gold gloves")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Ring_6stars_Gold.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found 6 stars gold ring")
            return screenPiece
        screenPiece = self.screen.Find("Shop_MysticalBook.png")
        if screenPiece is not None and self.magicShop.DidOpenEquipment(screenPiece) == False:
            self.Log("Found mystical book")
            return screenPiece
        return None

    def Summon(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            self.Log("Press Summon button")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Home_Summon))
        elif self.screen.screenType == ScreenType.SUMMON:
            screenPiece = self.screen.Find("Summon_BasicBookAvaiable.png")
            if screenPiece is not None:
                self.Log("Summon basic book")
                self.device.Touch(screenPiece.x + 127, screenPiece.y + 88)
                time.sleep(1)
                self.device.Touch(846, 360)
            else:
                screenPiece = self.screen.Find("Summon_MysteriousBookAvaiable.png")
                if screenPiece is not None:
                    self.Log("Summon mysterious book")
                    self.device.Touch(screenPiece.x + 127, screenPiece.y + 88)
                    time.sleep(1)
                    self.device.Touch(846, 360)
                else:
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.PlayDefault()
        else:
            self.PlayDefault()

    def PlayEventDungeon(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            self.Log("Press Event Dungeon button")
            screenPiece = self.screen.Find("GameHome_EventDungeon.png")
            if screenPiece is not None:
                self.device.Touch(screenPiece.x + 10, screenPiece.y + 10)
        elif self.screen.screenType == ScreenType.EVENT_DUNGEON:
            screenPiece = self.screen.Find("EventDungeon_Gold.png", 500000)
            if screenPiece is not None:
                screenPiece = self.screen.Find("EventDungeon_Gold_OutOfEntrance.png", 100000)
                if screenPiece is not None:
                    self.Log("Gold Dungeon is out of entrance. Go home...")
                    self.profile.SaveLastDatePlayEventDungeon()
                    self.profile.Save()
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.PlayDefault()
                else:
                    self.Log("Play Gold Dungeon")
                    self.device.Touch(513, 483)
            else:
                screenPiece = self.screen.Find("EventDungeon_EXP.png", 500000)
                if screenPiece is not None:
                    screenPiece = self.screen.Find("EventDungeon_EXP_OutOfEntrance.png", 100000)
                    if screenPiece is not None:
                        self.Log("EXP Dungeon is out of entrance. Go home...")
                        self.profile.SaveLastDatePlayEventDungeon()
                        self.profile.Save()
                        self.gameState = GameState.PROMOTION_BATTLE
                        self.PlayDefault()
                    else:
                        self.Log("Play EXP Dungeon")
                        self.device.Touch(923, 231)
                else:
                    self.PlayDefault()
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            self.Log("Auto place and start")
            self.device.Touch(767, 627)
            time.sleep(1)
            self.device.Touch(765, 141)
        else:
            self.PlayDefault()

    def PlayDefault(self):
        self.Log("PlayDefault")
        if self.screen.screenType == ScreenType.MAP:
            self.device.Touch(1190, 360)
        if self.screen.screenType == ScreenType.PVE_RESULT_VICTORY                      \
            or self.screen.screenType == ScreenType.EVENT_DUNGEON_RESULT_EXP            \
            or self.screen.screenType == ScreenType.EVENT_DUNGEON_RESULT_GOLD           \
            or self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY_RESULT_LOSE:
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Result_Home))
        elif self.screen.screenType == ScreenType.PVE_RESULT_REPEAT_RESULT:
            self.device.Touch(335, 77)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY      \
            or self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT      \
            or self.screen.screenType == ScreenType.BATTLE_LIST             \
            or self.screen.screenType == ScreenType.RIVAL_LIST              \
            or self.screen.screenType == ScreenType.BATTLE_RANKING          \
            or self.screen.screenType == ScreenType.BATTLE_DEFENSE_RECORD   \
            or self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB      \
            or self.screen.screenType == ScreenType.SHOP                    \
            or self.screen.screenType == ScreenType.SUMMON                  \
            or self.screen.screenType == ScreenType.EVENT_DUNGEON:
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Back))
        elif self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
            self.device.Touch(785, 460)
        elif self.screen.screenType == ScreenType.SUMMON_BASIC_DONE         \
            or self.screen.screenType == ScreenType.SUMMON_MYSTEROUS_DONE:
            self.device.Touch(1185, 361)
        elif self.screen.screenType == ScreenType.LEVEL_UP:
            self.device.Touch(500, 500)
        elif self.screen.screenType == ScreenType.SHOP_DIALOG_IS_OPENNING:
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_Cancel))
        elif self.screen.screenType == ScreenType.SHOP_DIALOG_PURCHASE_CONFIRMATION:
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_PurchaseConfirmation_Cancel))
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            self.gameState = GameState.OUT_OF_SHOES
            self.device.Touch(790, 474)
            if self.screen.Find("NotEnoughShoes_At_GuardianPlacement.png", 2000000) is not None:
                self.Log("Not enough shoes at guardian placement. Find more shoes...")
                self.device.Touch(46, 51)
            elif self.screen.Find("NotEnoughShoes_At_Result.png") is not None:
                self.Log("Not enough shoes at result. Find more shoes...")
                self.device.Touch(1197, 663)
            else:
                self.Log("Not enough shoes. Close the pop-up")
        elif self.screen.screenType == ScreenType.EVENT_DUNGEON_OUT_OF_ENTRANCE_POPUP:
            self.device.Touch(784, 356)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY_LOSE:
            self.device.Touch(788, 472)
        else:
            self.Log("Idle")

    def AutoTouch(self, autoTime = 2):
        maxTime = autoTime * 60
        interval = 5
        currentTime = 0
        while (currentTime < maxTime):
            tick = time.time()
            self.device.Touch(1200, 425)
            newTick = time.time()
            adbTime = newTick - tick
            sleepTime = interval - adbTime
            if sleepTime < 0:
                currentTime += adbTime
                sleepTime = 0
            else:
                currentTime += interval
            remainingTime = maxTime - currentTime
            self.Log("Auto touch: " + str(remainingTime // 60).zfill(2) + ":" + str(remainingTime % 60).zfill(2))
            time.sleep(sleepTime)

    def Log(self, log):
        print("[GameManager] " + log)
        return None
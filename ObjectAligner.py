import maya.cmds as mc


def Align(*args):
	lst = mc.ls(sl=True)
	cnt = len(lst)

	tar1 = mc.textField(stt, q=True, text=True)
	tar2 = mc.textField(end, q=True, text=True)
	tar1_trs = mc.xform(tar1, q=True, ws=True, rp=True)
	tar2_trs = mc.xform(tar2, q=True, ws=True, rp=True)

	trsx = (tar2_trs[0] - tar1_trs[0]) / (cnt + 1)
	trsy = (tar2_trs[1] - tar1_trs[1]) / (cnt + 1)
	trsz = (tar2_trs[2] - tar1_trs[2]) / (cnt + 1)

	for i in range(cnt):
		j = i + 1
		mc.setAttr('{}.t'.format(lst[i]), tar1_trs[0] + trsx*j, tar1_trs[1] + trsy*j, tar1_trs[2] + trsz*j)
		rop = mc.xform(lst[i], q=True, rp=True)
		if rop != [0, 0, 0]:
			mc.setAttr('{}.t'.format(lst[i]), tar1_trs[0] - rop[0] + trsx*j, tar1_trs[1] - rop[1] + trsy*j, tar1_trs[2] - rop[2] + trsz*j)


def stt_set(*args):
	global sst, tar
	sub = mc.ls(sl=True)
	sst = mc.textField(stt, e=True, text='{}'.format(sub[0]))
	if len(sub) > 1:
		tar = mc.textField(end, e=True, text='{}'.format(sub[1]))

def end_set(*args):
	global sst, tar
	sub = mc.ls(sl=True)
	tar = mc.textField(end, e=True, text='{}'.format(sub[0]))
	if len(sub) > 1:
		sst = mc.textField(stt, e=True, text='{}'.format(sub[1]))

def mainWin():
	global stt, end
	if mc.window('ObjectAligner', exists=True):
		mc.deleteUI('ObjectAligner')
	
	createWin = mc.window('ObjectAligner', t='Object Aligner', widthHeight=(300, 117))
	mc.window('ObjectAligner', e=True, widthHeight=(300, 117))
	mc.columnLayout(adj=True)
	
	mc.frameLayout(l='Range to Alignment')
	mc.rowLayout(nc=3, cat=[(1, 'left', 31), (2, 'left', 5)])
	mc.text('start :')
	stt = mc.textField('stt', w=170)
	mc.button(l='set', w=50, h=20, c=stt_set)
	mc.setParent('..')
	mc.rowLayout(nc=3, cat=[(1, 'left', 38), (2, 'left', 5)])
	mc.text('end :')
	end = mc.textField('end', w=170)
	mc.button(l='set', w=50, h=20, c=end_set)
	mc.setParent('..')
	mc.button(l='Execution', w=300, h=30, c=Align)
	
	mc.showWindow(createWin)

def consoleKey():
	mainWin()

consoleKey()
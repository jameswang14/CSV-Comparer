import csv
import wx
import os
wildcard = "All files (*.*) | *.*"

class MainFrame(wx.Frame):
	def __init__(self,parent, title):
		super(MainFrame, self).__init__(parent, title=title, size=(600,300))
		self.InitUI()
	def InitUI(self):
		hbox = wx.BoxSizer(wx.VERTICAL)
		gs1 = wx.GridSizer(1,2,0,0)
		gs2 = wx.GridSizer(1,2,0,0)
		gs3 = wx.GridSizer(1,2,0,0)
		gs4 = wx.GridSizer(1,2,0,0)
		file1_name = wx.StaticText(self, label="Input File 1 Name (master file)")
		file2_name = wx.StaticText(self, label="Input File 2 Name (most recent file)")
		file3_name = wx.StaticText(self, label="Output File Name (appends)")
		self.status = wx.StaticText(self, label="")

		self.file1Field = wx.TextCtrl(self, size = (300,20))
		self.file2Field = wx.TextCtrl(self, size = (300,20))
		self.file3Field = wx.TextCtrl(self, size = (300,20))
		
		browseFile1 = wx.Button(self, -1, "Browse File")
		browseFile2 = wx.Button(self, -1, "Browse File")
		browseFile3 = wx.Button(self, -1, "Append to File")
		run = wx.Button(self,-1,"Run")
		
		gs1.AddMany([(self.file1Field),(browseFile1)])
		gs2.AddMany([(self.file2Field),(browseFile2)])
		gs3.AddMany([(self.file3Field),(browseFile3)])
		gs4.AddMany([(run),(self.status)])

		hbox.Add(file1_name, proportion=1, flag=wx.ALL|wx.EXPAND, border = 0)
		hbox.Add(gs1, proportion=1, flag=wx.ALL, border = 0)
		hbox.Add(file2_name, proportion=1, flag=wx.ALL|wx.EXPAND, border = 0)
		hbox.Add(gs2, proportion=1,flag=wx.ALL)
		hbox.Add(file3_name, proportion=1, flag=wx.ALL|wx.EXPAND, border = 0)
		hbox.Add(gs3, proportion=1)
		hbox.Add(gs4, proportion=1)
		self.SetSizer(hbox)


		browseFile1.Bind(wx.EVT_BUTTON,self.onClickBrowseFile1)
		browseFile2.Bind(wx.EVT_BUTTON,self.onClickBrowseFile2)
		browseFile3.Bind(wx.EVT_BUTTON,self.onClickSaveItem)
		run.Bind(wx.EVT_BUTTON,self.onClickRemove)

		self.Show()
	def onClickBrowseFile1(self,e):
		dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            style=wx.OPEN | wx.CHANGE_DIR
            )
		if dlg.ShowModal() == wx.ID_OK:
            #Use GetPaths() for multiple files
			paths = dlg.GetPath()
			self.file1Field.SetValue(paths)
		dlg.Destroy()

	def onClickBrowseFile2(self,e):
		dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            style=wx.OPEN | wx.CHANGE_DIR
            )
		if dlg.ShowModal() == wx.ID_OK:
            #Use GetPaths() for multiple files
			paths = dlg.GetPath()
			self.file2Field.SetValue(paths)
		dlg.Destroy()

	def onClickSaveItem(self,e):
		dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", style=wx.SAVE|wx.CHANGE_DIR
            )
		dlg.SetFilename(self.file3Field.GetValue())

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			self.file3Field.SetValue(path)
		dlg.Destroy()

	def onClickRemove(self, e):
		if(self.file1Field.IsEmpty()):
			self.status.SetLabel("No File 1 Specified")
		elif(self.file2Field.IsEmpty()):
			self.status.SetLabel("No File 2 Specified")
		elif(self.file3Field.IsEmpty()):
			self.status.SetLabel("No Output File Specified")
		else:
			removeDup(self.file1Field.GetValue(), self.file2Field.GetValue(), self.file3Field.GetValue())
			self.status.SetLabel("Done")

def removeDup(file1, file2, outfile):
	with open(file1,'r') as in_file1, open(file2,'r') as in_file2, open(outfile,'a') as out_file:
		seen = set()
		for line in in_file1:
			seen.add(line)
		for line in in_file2:
			if line in seen:
				continue
			else:
				out_file.write(line)

app = wx.App()
MainFrame(None, title="Remove CSV Duplicates")
app.MainLoop()

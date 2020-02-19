from burp import IBurpExtender
from burp import ITab

from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing import JSplitPane


class BurpExtender(IBurpExtender, ITab):
    #
    # implement IBurpExtender
    #

    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Ishikawa")

        self._callbacks = callbacks
        self.initializeGUI()

        # obtain our output and error streams
        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)

        stdout.println("Ishikawa output")
        callbacks.issueAlert("Ishikawa alerts")

        callbacks.addSuiteTab(self)

    #
    # implement ITab
    #

    def getTabCaption(self):
        return "Ishikawa"

    def getUiComponent(self):
        return self._splitpane

    # Init GUI
    def initializeGUI(self):
        # copy from lmt-swallow
        self._splitpane = JSplitPane()
        self._callbacks.customizeUiComponent(self._splitpane)

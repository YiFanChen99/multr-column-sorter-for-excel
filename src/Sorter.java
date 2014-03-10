public class Sorter {

	static int rowCount;
	// static int[] indexes;
	static String[] keys = returnKeys();
	static int[] lines = returnLines();

	public static void main(String[] args) {
		rowCount = keys.length;
		if (rowCount != lines.length) {
			throw new IllegalArgumentException();
		}

		insertionSort();

		for (int i = 0; i < rowCount; i++) {
			System.out.println(keys[i] + "\t" + lines[i]);
		}
	}

	/**
	 * 基本的 insertionSort，不使用
	 */
	private static void insertionSort() {
		int i, j;
		for (i = 1; i < rowCount; i++) {
			String thisKey = keys[i];
			int thisLine = lines[i];
			for (j = i - 1; j >= 0; j--) {
				if (thisKey.compareTo(keys[j]) >= 0) {
					break;
				}
				keys[j + 1] = keys[j];
				lines[j + 1] = lines[j];
			}
			keys[j + 1] = thisKey;
			lines[j + 1] = thisLine;
		}
	}

	private static String[] returnKeys() {
		String[] keys = {
				"org.apache.tools.ant.util.TeeOutputStream",
				"org.apache.tools.ant.taskdefs.email.UUMailer",
				"org.apache.tools.ant.input.DefaultInputHandler",
				"org.apache.tools.ant.taskdefs.rmic.SunRmic",
				"org.apache.tools.ant.taskdefs.optional.depend.AntAnalyzer",
				"org.apache.tools.ant.taskdefs.optional.net.TelnetTask",
				"org.apache.tools.ant.taskdefs.email.Message",
				"org.apache.tools.ant.types.resources.ZipResource",
				"org.apache.tools.ant.taskdefs.email.PlainMailer",
				"org.apache.tools.ant.filters.util.ChainReaderHelper",
				"org.apache.tools.ant.taskdefs.optional.junit.AggregateTransformer",
				"org.apache.tools.ant.taskdefs.Pack",
				"org.apache.tools.ant.taskdefs.optional.PropertyFile",
				"org.apache.tools.ant.types.resources.AbstractClasspathResource",
				"org.apache.tools.ant.taskdefs.optional.PropertyFile",
				"org.apache.tools.ant.taskdefs.ExecuteJava",
				"org.apache.tools.ant.types.selectors.ContainsRegexpSelector",
				"org.apache.tools.ant.taskdefs.optional.PropertyFile",
				"org.apache.tools.ant.taskdefs.optional.splash.SplashTask",
				"org.apache.tools.ant.taskdefs.optional.ssh.ScpToMessage",
				"org.apache.tools.ant.taskdefs.optional.ssh.ScpFromMessage",
				"org.apache.tools.ant.taskdefs.optional.ssh.ScpFromMessage",
				"org.apache.tools.ant.util.depend.AbstractAnalyzer",
				"org.apache.tools.ant.util.SymbolicLinkUtils",
				"org.apache.tools.ant.taskdefs.optional.TraXLiaison",
				"org.apache.tools.mail.MailMessage",
				"org.apache.tools.ant.taskdefs.optional.net.RExecTask",
				"org.apache.tools.ant.taskdefs.optional.ssh.SSHExec",
				"org.apache.tools.ant.taskdefs.XSLTProcess",
				"org.apache.tools.ant.taskdefs.optional.testing.Funtest",
				"org.apache.tools.ant.AntClassLoader",
				"org.apache.tools.ant.taskdefs.Property",
				"org.apache.tools.ant.taskdefs.optional.net.FTPTaskMirrorImpl",
				"org.apache.tools.ant.taskdefs.Zip",
				"org.apache.tools.ant.taskdefs.optional.net.FTP",
				"org.apache.tools.ant.taskdefs.optional.ejb.GenericDeploymentTool",
				"org.apache.tools.ant.taskdefs.SQLExec",
				"org.apache.tools.ant.Main",
				"org.apache.tools.ant.taskdefs.Zip",
				"org.apache.tools.ant.taskdefs.optional.net.FTPTaskMirrorImpl",
				"org.apache.tools.ant.taskdefs.optional.junit.JUnitTask",
				"org.apache.tools.ant.taskdefs.optional.net.FTP",
				"org.apache.tools.ant.taskdefs.Jar",
				"org.apache.tools.ant.taskdefs.optional.net.FTPTaskMirrorImpl",
				"org.apache.tools.ant.taskdefs.Javac",
				"org.apache.tools.ant.taskdefs.optional.junit.JUnitTask",
				"org.apache.tools.ant.taskdefs.Zip" };
		return keys;
	}

	private static int[] returnLines() {
		int[] lines = { 50, 51, 69, 99, 102, 125, 135, 149, 158, 175, 178, 183,
				184, 188, 196, 202, 213, 250, 257, 270, 274, 275, 277, 277,
				303, 352, 382, 406, 436, 469, 501, 541, 650, 720, 749, 805,
				842, 844, 962, 1063, 1103, 1157, 1162, 1208, 1243, 1426, 1893 };
		return lines;
	}
}

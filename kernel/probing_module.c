#include <linux/module.h> /* Needed by all modules */
#include <linux/kernel.h> /* Needed for KERN_INFO */
#include <linux/init.h> /* Needed for the macros */

MODULE_LICENSE("GPL");
MODULE_AUTHOR("CyberArk Labs");
MODULE_DESCRIPTION("A simple probing LKM!");
MODULE_VERSION("0.3");

static int __init startprobing(void)
{

int *crc1 = (int *)0xffffffff9a841cd8; // address of crc of call_usermodehelper
int *crc2 = (int *)0xffffffff9a847308; // address of crc of printk

printk(KERN_EMERG "Loading probing module...\n");
printk(KERN_EMERG "CRC of call_UserModeHelper = 0x%x\n", *crc1);
printk(KERN_EMERG "CRC of printk = 0x%x\n", *crc2);

return 0;
}

static void __exit startprobing_end(void)
{
printk(KERN_EMERG "Goodbye!\n");
}

module_init(startprobing);
module_exit(startprobing_end);

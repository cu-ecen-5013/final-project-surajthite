
##############################################################
#
# LDD
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
LDD_VERSION = 2ac32ebb97fec656e8e1d9aeacef3feb724771bd
LDD_SITE = git@github.com:cu-ecen-5013/assignment-3-manual-kernel-and-root-filesystem-build-surajthite.git
LDD_SITE_METHOD = git

LDD_MODULE_SUBDIRS = aesd-char-driver
#LDD_MODULE_SUBDIRS += scull/

# define LDD_BUILD_CMDS
# 	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D) all 
# endef

# #TODO: Add required executables or scripts below
# define LDD_INSTALL_TARGET_CMDS
# 	$(INSTALL) -m 0755 $(@D)/aesdsocket $(TARGET_DIR)/usr/bin
# 	$(INSTALL) -m 0755 $(@D)/aesdsocket-start-stop.sh $(TARGET_DIR)/etc/init.d/S99aesdsocket
# 	$(INSTALL) -m 0755 $(@D)/writer $(TARGET_DIR)/bin
# 	$(INSTALL) -m 0755 $(@D)/tester.sh $(TARGET_DIR)/bin
# 	$(INSTALL) -m 0755 $(@D)/finder.sh $(TARGET_DIR)/bin
# endef

$(eval $(kernel-module))
$(eval $(generic-package))

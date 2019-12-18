#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

#define ENERGEST_CONF_ON 1

/* CC2538_RF_CONF_CHANNEL */
// default 0xD5
#ifndef CC2538_RF_CONF_TX_POWER
#define CC2538_RF_CONF_TX_POWER             0xBC
#endif 

/* USB serial takes space, free more space elsewhere */
#define SICSLOWPAN_CONF_FRAG 0
// default 1280
#define UIP_CONF_BUFFER_SIZE 160

/*******************************************************/
/******************* Configure TSCH ********************/
/*******************************************************/

// default (16 * CLOCK_SECOND)
#define TSCH_CONF_EB_PERIOD (4 * CLOCK_SECOND)
#define TSCH_CONF_MAX_EB_PERIOD (4 * CLOCK_SECOND)

// #define LOG_CONF_LEVEL_MAC                         LOG_LEVEL_DBG
// #define TSCH_LOG_CONF_PER_SLOT                     1

#endif /* PROJECT_CONF_H_ */


/*

+7 dBm 0xFF

+5 dBm 0xED

+3 dBm 0xD5

+1 dBm 0xC5

0 dBm 0xBc,....*/

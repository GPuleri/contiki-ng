#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

#define ENERGEST_CONF_ON 1

/* USB serial takes space, free more space elsewhere */
#define SICSLOWPAN_CONF_FRAG 0
// default 1280
#define UIP_CONF_BUFFER_SIZE 160

/*******************************************************/
/******************* Configure TSCH ********************/
/*******************************************************/

// default (16 * CLOCK_SECOND)
#define TSCH_CONF_EB_PERIOD (CLOCK_SECOND)
#define TSCH_CONF_MAX_EB_PERIOD (CLOCK_SECOND)

// #define LOG_CONF_LEVEL_MAC                         LOG_LEVEL_DBG
#define TSCH_LOG_CONF_PER_SLOT                     1

#endif /* PROJECT_CONF_H_ */

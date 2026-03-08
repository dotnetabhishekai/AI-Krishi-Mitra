# AI Krishi Mitra: Process Flow Diagrams 🌾

## Complete System Process Flow

```mermaid
flowchart TD
    subgraph "👨‍🌾 Farmer Input Layer"
        FI[Farmer Initiates Query]
        WA[💬 WhatsApp]
        VI[🎤 Voice Input]
        TI[📝 Text Input]
        II[📸 Image Input]
    end
    
    subgraph "🔍 Input Processing Layer"
        LD[🌐 Language Detection]
        STT[🎙️ Speech-to-Text]
        NLP[🧠 Natural Language Processing]
        CV[👁️ Computer Vision]
        IT[🔄 Input Translation]
    end
    
    subgraph "🧠 AI Processing Core"
        AE[🌱 Advisory Engine]
        KB[📚 Knowledge Base]
        FP[👤 Farmer Profile]
        WS[🌤️ Weather Service]
        RA[⚠️ Risk Assessment]
    end
    
    subgraph "📊 Data Sources"
        IMD[🌡️ IMD Weather API]
        ARD[🔬 Agricultural Research DB]
        HD[📈 Historical Data]
        LD_DB[🗺️ Location Data]
    end
    
    subgraph "💡 Response Generation"
        RG[📝 Response Generation]
        LP[🌐 Language Processing]
        TTS[🔊 Text-to-Speech]
        RF[📋 Response Formatting]
    end
    
    subgraph "📤 Output Delivery"
        VO[🎵 Voice Output]
        TO[📝 Text Output]
        IO[📊 Image/Chart Output]
        PN[🔔 Push Notification]
    end
    
    subgraph "💾 Data Management"
        DS[💾 Data Storage]
        OS[📴 Offline Sync]
        CR[🔄 Conflict Resolution]
        BU[☁️ Backup]
    end
    
    %% Flow connections
    FI --> WA
    WA --> VI
    WA --> TI
    WA --> II
    
    VI --> LD
    TI --> LD
    II --> CV
    LD --> STT
    LD --> NLP
    STT --> NLP
    NLP --> IT
    CV --> IT
    
    IT --> AE
    AE --> KB
    AE --> FP
    AE --> WS
    AE --> RA
    
    WS --> IMD
    KB --> ARD
    FP --> HD
    RA --> LD_DB
    
    AE --> RG
    RG --> LP
    LP --> TTS
    LP --> RF
    
    TTS --> VO
    RF --> TO
    RF --> IO
    RF --> PN
    
    VO --> WA
    TO --> WA
    IO --> WA
    
    AE --> DS
    DS --> OS
    OS --> CR
    DS --> BU
    
    style FI fill:#4CAF50
    style AE fill:#FF9800
    style IMD fill:#2196F3
    style VO fill:#9C27B0
```

## Voice Query Process Flow

```mermaid
flowchart TD
    subgraph "🎤 Voice Input Processing"
        VR[🎙️ Voice Recording Starts]
        AQ[🔊 Audio Quality Check]
        LD[🌐 Language Detection]
        STT[📝 Speech-to-Text Conversion]
        CA[✅ Confidence Assessment]
    end
    
    subgraph "🧠 Query Understanding"
        NLP[🔍 Natural Language Processing]
        IC[🎯 Intent Classification]
        EE[📋 Entity Extraction]
        CU[🤔 Context Understanding]
    end
    
    subgraph "💡 Response Generation"
        KB[📚 Knowledge Base Query]
        FP[👤 Farmer Profile Lookup]
        WD[🌤️ Weather Data Fetch]
        RG[📝 Response Generation]
        TL[🌐 Response Translation]
    end
    
    subgraph "🔊 Audio Response"
        TTS[🎵 Text-to-Speech]
        VO[🔊 Voice Output]
        FB[📊 Feedback Collection]
    end
    
    %% Decision points
    AQ -->|Good Quality| LD
    AQ -->|Poor Quality| RR[🔄 Request Re-recording]
    RR --> VR
    
    CA -->|High Confidence| NLP
    CA -->|Low Confidence| CR[❓ Clarification Request]
    CR --> TTS
    
    IC -->|Agricultural Query| EE
    IC -->|Weather Query| WD
    IC -->|General Query| KB
    IC -->|Unknown Intent| UH[❓ Unknown Handler]
    
    %% Main flow
    VR --> AQ
    LD --> STT
    STT --> CA
    NLP --> IC
    EE --> CU
    CU --> KB
    KB --> FP
    FP --> RG
    WD --> RG
    RG --> TL
    TL --> TTS
    TTS --> VO
    VO --> FB
    
    %% Error handling
    UH --> TTS
    
    style VR fill:#4CAF50
    style NLP fill:#2196F3
    style RG fill:#FF9800
    style VO fill:#9C27B0
```

## WhatsApp Integration Process Flow

```mermaid
flowchart TD
    subgraph "💬 WhatsApp Gateway"
        WM[📱 WhatsApp Message Received]
        MT[🔍 Message Type Detection]
        WH[🔗 Webhook Processing]
    end
    
    subgraph "📝 Message Processing"
        TM[📝 Text Message]
        VM[🎤 Voice Message]
        IM[📸 Image Message]
        DM[📄 Document Message]
    end
    
    subgraph "🔄 Processing Pipeline"
        MP[⚙️ Message Processing]
        UP[👤 User Profile Lookup]
        SP[📊 Session Processing]
        QR[⚡ Quick Reply Handler]
    end
    
    subgraph "💡 Response Generation"
        AE[🧠 Advisory Engine]
        RF[📋 Response Formatting]
        MF[💬 WhatsApp Message Format]
    end
    
    subgraph "📤 Response Delivery"
        TR[📝 Text Response]
        VR[🎵 Voice Response]
        IR[📊 Image Response]
        QRB[⚡ Quick Reply Buttons]
    end
    
    %% Flow connections
    WM --> MT
    MT --> WH
    WH --> TM
    WH --> VM
    WH --> IM
    WH --> DM
    
    TM --> MP
    VM --> MP
    IM --> MP
    DM --> MP
    
    MP --> UP
    UP --> SP
    SP --> QR
    QR --> AE
    
    AE --> RF
    RF --> MF
    
    MF --> TR
    MF --> VR
    MF --> IR
    MF --> QRB
    
    %% Decision flows
    MT -->|Text| TM
    MT -->|Voice| VM
    MT -->|Image| IM
    MT -->|Document| DM
    
    style WM fill:#25D366
    style AE fill:#FF9800
    style TR fill:#4CAF50
```

## Offline-Online Synchronization Flow

```mermaid
flowchart TD
    subgraph "📴 Offline Mode"
        OQ[📱 Offline Query]
        LC[💾 Local Cache Check]
        LD[📊 Local Data Processing]
        QQ[📋 Query Queue]
    end
    
    subgraph "🔄 Sync Detection"
        CD[📶 Connectivity Detection]
        SD[🔄 Sync Decision]
        PQ[📋 Pending Queue Check]
    end
    
    subgraph "☁️ Online Sync"
        DS[📤 Data Send]
        DR[📥 Data Receive]
        CR[⚖️ Conflict Resolution]
        MU[🔄 Merge Updates]
    end
    
    subgraph "💾 Data Management"
        CU[💾 Cache Update]
        LS[💾 Local Storage]
        BU[☁️ Backup Creation]
        VS[✅ Version Sync]
    end
    
    %% Offline flow
    OQ --> LC
    LC -->|Cache Hit| LD
    LC -->|Cache Miss| QQ
    LD --> LS
    QQ --> LS
    
    %% Sync detection
    CD -->|Online| SD
    CD -->|Offline| OQ
    SD --> PQ
    
    %% Online sync
    PQ -->|Has Pending| DS
    PQ -->|No Pending| DR
    DS --> DR
    DR --> CR
    CR --> MU
    
    %% Data management
    MU --> CU
    CU --> LS
    LS --> BU
    BU --> VS
    
    %% Decision points
    LC -->|Available| LD
    LC -->|Unavailable| QQ
    CR -->|No Conflict| CU
    CR -->|Conflict Found| CF[⚠️ Conflict Handler]
    CF --> CU
    
    style OQ fill:#9E9E9E
    style CD fill:#4CAF50
    style DS fill:#2196F3
    style CU fill:#FF9800
```

## Risk Alert Process Flow

```mermaid
flowchart TD
    subgraph "📊 Data Collection"
        WD[🌤️ Weather Data]
        SD[🌱 Sensor Data]
        FD[👨‍🌾 Farmer Reports]
        HD[📈 Historical Data]
    end
    
    subgraph "🔍 Risk Analysis"
        DA[📊 Data Analysis]
        PA[🔮 Predictive Analytics]
        RA[⚠️ Risk Assessment]
        SL[📊 Severity Level]
    end
    
    subgraph "🚨 Alert Generation"
        AT[🏷️ Alert Type Classification]
        AG[📝 Alert Generation]
        LP[🌐 Language Processing]
        PC[👥 Priority Classification]
    end
    
    subgraph "📤 Alert Delivery"
        PN[🔔 Push Notification]
        WA[💬 WhatsApp Alert]
        VA[🔊 Voice Alert]
        SM[📱 SMS Backup]
    end
    
    subgraph "📊 Response Tracking"
        AR[📥 Alert Received]
        AA[✅ Alert Acknowledged]
        AT_Track[📊 Action Taken]
        FB[📊 Feedback Collection]
    end
    
    %% Flow connections
    WD --> DA
    SD --> DA
    FD --> DA
    HD --> DA
    
    DA --> PA
    PA --> RA
    RA --> SL
    
    SL --> AT
    AT --> AG
    AG --> LP
    LP --> PC
    
    PC -->|Critical| PN
    PC -->|High| WA
    PC -->|Medium| VA
    PC -->|Low| SM
    
    PN --> AR
    WA --> AR
    VA --> AR
    SM --> AR
    
    AR --> AA
    AA --> AT_Track
    AT_Track --> FB
    
    %% Decision points
    SL -->|Critical| CR[🚨 Critical Alert]
    SL -->|High| HR[⚠️ High Alert]
    SL -->|Medium| MR[📊 Medium Alert]
    SL -->|Low| LR[ℹ️ Low Alert]
    
    CR --> PN
    HR --> WA
    MR --> VA
    LR --> SM
    
    style WD fill:#03A9F4
    style RA fill:#FF5722
    style PN fill:#F44336
    style FB fill:#4CAF50
```

## Farmer Onboarding Process Flow

```mermaid
flowchart TD
    subgraph "📱 Registration"
        SI[📱 System Introduction]
        LR[🌐 Language Registration]
        PI[👤 Personal Information]
        FI[🌾 Farm Information]
    end
    
    subgraph "🎤 Voice Setup"
        VT[🎙️ Voice Test]
        LS[🌐 Language Selection]
        VA[🔊 Voice Accuracy Test]
        VP[👤 Voice Profile Creation]
    end
    
    subgraph "🌾 Crop Configuration"
        CT[🌱 Crop Type Selection]
        CD[📅 Crop Details Entry]
        CC[📅 Crop Calendar Setup]
        GS[📊 Growth Stage Setting]
    end
    
    subgraph "📍 Location Setup"
        LG[📍 Location Grant]
        WS[🌤️ Weather Station Link]
        RS[🗺️ Regional Settings]
        LS_Config[🌐 Local Services Config]
    end
    
    subgraph "✅ Verification"
        PV[✅ Profile Verification]
        TQ[❓ Test Query]
        TR[📝 Test Response]
        OC[✅ Onboarding Complete]
    end
    
    %% Flow connections
    SI --> LR
    LR --> PI
    PI --> FI
    
    FI --> VT
    VT --> LS
    LS --> VA
    VA --> VP
    
    VP --> CT
    CT --> CD
    CD --> CC
    CC --> GS
    
    GS --> LG
    LG --> WS
    WS --> RS
    RS --> LS_Config
    
    LS_Config --> PV
    PV --> TQ
    TQ --> TR
    TR --> OC
    
    %% Decision points
    VA -->|Pass| VP
    VA -->|Fail| VT
    TQ -->|Success| TR
    TQ -->|Fail| CT
    
    style SI fill:#4CAF50
    style VP fill:#2196F3
    style CC fill:#FF9800
    style OC fill:#8BC34A
```

## Emergency Response Process Flow

```mermaid
flowchart TD
    subgraph "🚨 Emergency Detection"
        ED[🚨 Emergency Detected]
        ET[🏷️ Emergency Type]
        SA[📊 Severity Assessment]
        UL[📍 User Location]
    end
    
    subgraph "⚡ Immediate Response"
        IR[⚡ Immediate Response]
        EA[🚨 Emergency Alert]
        PS[🛡️ Protective Steps]
        EC[📞 Emergency Contacts]
    end
    
    subgraph "👨‍⚕️ Expert Escalation"
        EE[👨‍🎓 Expert Escalation]
        EA_Expert[📧 Expert Alert]
        ER[📝 Expert Response]
        FU[📞 Follow-up]
    end
    
    subgraph "📊 Recovery Support"
        RA[📊 Recovery Assessment]
        RG[📋 Recovery Guidance]
        RS[🔄 Recovery Support]
        LM[📊 Long-term Monitoring]
    end
    
    %% Flow connections
    ED --> ET
    ET --> SA
    SA --> UL
    
    UL --> IR
    IR --> EA
    EA --> PS
    PS --> EC
    
    SA -->|Critical| EE
    EE --> EA_Expert
    EA_Expert --> ER
    ER --> FU
    
    PS --> RA
    FU --> RA
    RA --> RG
    RG --> RS
    RS --> LM
    
    %% Decision points
    ET -->|Weather| WE[🌪️ Weather Emergency]
    ET -->|Pest| PE[🐛 Pest Emergency]
    ET -->|Disease| DE[🦠 Disease Emergency]
    ET -->|Market| ME[💰 Market Emergency]
    
    WE --> IR
    PE --> IR
    DE --> IR
    ME --> IR
    
    style ED fill:#F44336
    style IR fill:#FF5722
    style EE fill:#9C27B0
    style LM fill:#4CAF50
```

---

## Process Flow Summary

These process flows demonstrate how AI Krishi Mitra handles:

1. **Complete System Flow** - End-to-end user interaction
2. **Voice Processing** - Speech recognition and response
3. **WhatsApp Integration** - Multi-modal messaging
4. **Offline Synchronization** - Seamless online/offline transitions
5. **Risk Alerts** - Proactive warning system
6. **Farmer Onboarding** - User registration and setup
7. **Emergency Response** - Crisis management workflow

Each flow is designed to ensure reliable, accessible, and effective agricultural advisory services for India's small and marginal farmers.
<#######<Script>#######>
<#######<Header>#######>
# Name: Get-FutureFinanceProjection
# Copyright: Gerry Williams (https://automationadmin.com)
# License: MIT License (https://opensource.org/licenses/mit)
# Script Modified from: n/a
<#######</Header>#######>
<#######<Body>#######>
Function Get-FutureFinanceProjection
{
   <#
.Synopsis
Based on variables, project's possible future balances.
.Description
Based on variables, project's possible future balances.
.Example
With these vars:

$YearlySavings = 1200
$YearlyRetirement = 1200
$YearlyBrokerage = 600
$YearlyCrypto = 600

$CurrentYear = 2021
$CurrentSavings = 1000
$CurrentRetirement = 1520
$CurrentCrypto = 240
$CurrentBrokerage = 1000

$RetirementInterest = 0.03
$CryptoInterest = 0.03
$BrokerageInterest = 0.03

$SavingsTarget = 20000
$Millionair = 1000000

##################################################

Output will look like:

Saving: $100.00 into Savings, $100.00 into Retirement, $50.00 into Brokerage, and $50.00 into Crypto, each month would net you...

Date Savings    Retirement Brokerage  Crypto     Total       Notes
---- -------    ---------- ---------  ------     -----       -----
2021 $1,000.00  $1,520.00  $1,000.00  $240.00    $3,760.00
2022 $2,200.00  $2,801.60  $1,648.00  $865.20    $7,514.80
2023 $3,400.00  $4,121.65  $2,315.44  $1,509.16  $11,346.24
2024 $4,600.00  $5,481.30  $3,002.90  $2,172.43  $15,256.63
2025 $5,800.00  $6,881.74  $3,710.99  $2,855.60  $19,248.33
2026 $7,000.00  $8,324.19  $4,440.32  $3,559.27  $23,323.78
2027 $8,200.00  $9,809.91  $5,191.53  $4,284.05  $27,485.49
2028 $9,400.00  $11,340.21 $5,965.28  $5,030.57  $31,736.06
2029 $10,600.00 $12,916.42 $6,762.23  $5,799.49  $36,078.14
2030 $11,800.00 $14,539.91 $7,583.10  $6,591.47  $40,514.48
2031 $13,000.00 $16,212.11 $8,428.59  $7,407.22  $45,047.92
2032 $14,200.00 $17,934.47 $9,299.45  $8,247.43  $49,681.36
2033 $15,400.00 $19,708.51 $10,196.44 $9,112.86  $54,417.80
2034 $16,600.00 $21,535.76 $11,120.33 $10,004.24 $59,260.33
2035 $17,800.00 $23,417.83 $12,071.94 $10,922.37 $64,212.14
2036 $19,000.00 $25,356.37 $13,052.10 $11,868.04 $69,276.51
2037 $20,200.00 $27,353.06 $14,061.66 $12,842.08 $74,456.80  Savings requirement met
2038 $21,400.00 $29,409.65 $15,101.51 $13,845.34 $79,756.50  Savings requirement met
2039 $22,600.00 $31,527.94 $16,172.55 $14,878.70 $85,179.20  Savings requirement met
2040 $23,800.00 $33,709.78 $17,275.73 $15,943.07 $90,728.58  Savings requirement met
2041 $25,000.00 $35,957.07 $18,412.00 $17,039.36 $96,408.43  Savings requirement met
2042 $26,200.00 $38,271.78 $19,582.36 $18,168.54 $102,222.69 Savings requirement met
2043 $27,400.00 $40,655.94 $20,787.83 $19,331.60 $108,175.37 Savings requirement met
2044 $28,600.00 $43,111.62 $22,029.47 $20,529.54 $114,270.63 Savings requirement met
2045 $29,800.00 $45,640.96 $23,308.35 $21,763.43 $120,512.75 Savings requirement met
2046 $31,000.00 $48,246.19 $24,625.60 $23,034.33 $126,906.13 Savings requirement met
2047 $32,200.00 $50,929.58 $25,982.37 $24,343.36 $133,455.31 Savings requirement met
2048 $33,400.00 $53,693.47 $27,379.84 $25,691.66 $140,164.97 Savings requirement met
2049 $34,600.00 $56,540.27 $28,819.24 $27,080.41 $147,039.92 Savings requirement met

.Notes
Version History:
2021-11-01: Initial
#>

   [Cmdletbinding()]
    
   Param
   (
   )
    
   Begin
   {       
      ####################<Default Begin Block>####################
      # Force verbose because Write-Output doesn't look well in transcript files
      $VerbosePreference = "Continue"
        
      [String]$Logfile = $PSScriptRoot + '\PSLogs\' + (Get-Date -Format "yyyy-MM-dd") +
      "-" + $MyInvocation.MyCommand.Name + ".log"
        
      Function Write-Log
      {
         <#
            .Synopsis
            This writes objects to the logfile and to the screen with optional coloring.
            .Parameter InputObject
            This can be text or an object. The function will convert it to a string and verbose it out.
            Since the main function forces verbose output, everything passed here will be displayed on the screen and to the logfile.
            .Parameter Color
            Optional coloring of the input object.
            .Example
            Write-Log "hello" -Color "yellow"
            Will write the string "VERBOSE: YYYY-MM-DD HH: Hello" to the screen and the logfile.
            NOTE that Stop-Log will then remove the string 'VERBOSE :' from the logfile for simplicity.
            .Example
            Write-Log (cmd /c "ipconfig /all")
            Will write the string "VERBOSE: YYYY-MM-DD HH: ****ipconfig output***" to the screen and the logfile.
            NOTE that Stop-Log will then remove the string 'VERBOSE :' from the logfile for simplicity.
            .Notes
            2018-06-24: Initial script
            #>
            
         Param
         (
            [Parameter(Mandatory = $true, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true, Position = 0)]
            [PSObject]$InputObject,
                
            # I usually set this to = "Green" since I use a black and green theme console
            [Parameter(Mandatory = $False, Position = 1)]
            [Validateset("Black", "Blue", "Cyan", "Darkblue", "Darkcyan", "Darkgray", "Darkgreen", "Darkmagenta", "Darkred", `
                  "Darkyellow", "Gray", "Green", "Magenta", "Red", "White", "Yellow")]
            [String]$Color = "White"
         )
            
         $ConvertToString = Out-String -InputObject $InputObject -Width 100
            
         If ($($Color.Length -gt 0))
         {
            $previousForegroundColor = $Host.PrivateData.VerboseForegroundColor
            $Host.PrivateData.VerboseForegroundColor = $Color
            Write-Verbose -Message "$(Get-Date -Format "yyyy-MM-dd hh:mm:ss tt"): $ConvertToString"
            $Host.PrivateData.VerboseForegroundColor = $previousForegroundColor
         }
         Else
         {
            Write-Verbose -Message "$(Get-Date -Format "yyyy-MM-dd hh:mm:ss tt"): $ConvertToString"
         }
            
      }

      Function Start-Log
      {
         <#
            .Synopsis
            Creates the log file and starts transcribing the session.
            .Notes
            2018-06-24: Initial script
            #>
            
         # Create transcript file if it doesn't exist
         If (!(Test-Path $Logfile))
         {
            New-Item -Itemtype File -Path $Logfile -Force | Out-Null
         }
        
         # Clear it if it is over 10 MB
         [Double]$Sizemax = 10485760
         $Size = (Get-Childitem $Logfile | Measure-Object -Property Length -Sum) 
         If ($($Size.Sum -ge $SizeMax))
         {
            Get-Childitem $Logfile | Clear-Content
            Write-Verbose "Logfile has been cleared due to size"
         }
         Else
         {
            Write-Verbose "Logfile was less than 10 MB"   
         }
         Start-Transcript -Path $Logfile -Append 
         Write-Log "####################<Function>####################"
         Write-Log "Function started on $env:COMPUTERNAME"

      }
        
      Function Stop-Log
      {
         <#
            .Synopsis
            Stops transcribing the session and cleans the transcript file by removing the fluff.
            .Notes
            2018-06-24: Initial script
            #>
            
         Write-Log "Function completed on $env:COMPUTERNAME"
         Write-Log "####################</Function>####################"
         Stop-Transcript
       
         # Now we will clean up the transcript file as it contains filler info that needs to be removed...
         $Transcript = Get-Content $Logfile -raw

         # Create a tempfile
         $TempFile = $PSScriptRoot + "\PSLogs\temp.txt"
         New-Item -Path $TempFile -ItemType File | Out-Null
			
         # Get all the matches for PS Headers and dump to a file
         $Transcript | 
         Select-String '(?smi)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*([\S\s]*?)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*' -AllMatches | 
         ForEach-Object { $_.Matches } | 
         ForEach-Object { $_.Value } | 
         Out-File -FilePath $TempFile -Append

         # Compare the two and put the differences in a third file
         $m1 = Get-Content -Path $Logfile
         $m2 = Get-Content -Path $TempFile
         $all = Compare-Object -ReferenceObject $m1 -DifferenceObject $m2 | Where-Object -Property Sideindicator -eq '<='
         $Array = [System.Collections.Generic.List[PSObject]]@()
         foreach ($a in $all)
         {
            [void]$Array.Add($($a.InputObject))
         }
         $Array = $Array -replace 'VERBOSE: ', ''

         Remove-Item -Path $Logfile -Force
         Remove-Item -Path $TempFile -Force
         # Finally, put the information we care about in the original file and discard the rest.
         $Array | Out-File $Logfile -Append -Encoding ASCII
            
      }
        
      Start-Log

      Function Set-Console
      {
         <# 
        .Synopsis
        Function to set console colors just for the session.
        .Description
        Function to set console colors just for the session.
        This function sets background to black and foreground to green.
        Verbose is DarkCyan which is what I use often with logging in scripts.
        I mainly did this because darkgreen does not look too good on blue (Powershell defaults).
        .Notes
        2017-10-19: v1.0 Initial script 
        #>
        
         Function Test-IsAdmin
         {
            <#
                .Synopsis
                Determines whether or not the user is a member of the local Administrators security group.
                .Outputs
                System.Bool
                #>

            [CmdletBinding()]
    
            $Identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
            $Principal = new-object System.Security.Principal.WindowsPrincipal(${Identity})
            $IsAdmin = $Principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
            Write-Output -InputObject $IsAdmin
         }

         $console = $host.UI.RawUI
         If (Test-IsAdmin)
         {
            $console.WindowTitle = "Administrator: Powershell"
         }
         Else
         {
            $console.WindowTitle = "Powershell"
         }
         $Background = "Black"
         $Foreground = "Green"
         $Messages = "DarkCyan"
         $Host.UI.RawUI.BackgroundColor = $Background
         $Host.UI.RawUI.ForegroundColor = $Foreground
         $Host.PrivateData.ErrorForegroundColor = $Messages
         $Host.PrivateData.ErrorBackgroundColor = $Background
         $Host.PrivateData.WarningForegroundColor = $Messages
         $Host.PrivateData.WarningBackgroundColor = $Background
         $Host.PrivateData.DebugForegroundColor = $Messages
         $Host.PrivateData.DebugBackgroundColor = $Background
         $Host.PrivateData.VerboseForegroundColor = $Messages
         $Host.PrivateData.VerboseBackgroundColor = $Background
         $Host.PrivateData.ProgressForegroundColor = $Messages
         $Host.PrivateData.ProgressBackgroundColor = $Background
         Clear-Host
      }
      Set-Console

      ####################</Default Begin Block>####################

   }
    
   Process
   {   
      Try
      {
         
         # Params
         #############################################
         $YearlySavings = 1200
         $YearlyRetirement = 1200
         $YearlyBrokerage = 600
         $YearlyCrypto = 600

         $CurrentYear = 2021
         $CurrentSavings = 1000
         $CurrentRetirement = 1520
         $CurrentCrypto = 240
         $CurrentBrokerage = 1000

         $RetirementInterest = 0.03
         $CryptoInterest = 0.03
         $BrokerageInterest = 0.03

         $SavingsTarget = 20000
         $Millionair = 1000000
         #############################################

         $DollarSavings = "{0:C2}" -f $CurrentSavings
         $DollarRetirement = "{0:C2}" -f $CurrentRetirement
         $DollarBrokerage = "{0:C2}" -f $CurrentBrokerage
         $DollarCrypto = "{0:C2}" -f $CurrentCrypto
         $CurrentTotal = $CurrentSavings + $CurrentRetirement + $CurrentBrokerage + $CurrentCrypto
         $DollarTotal = "{0:C2}" -f $CurrentTotal

         $DisplayYearlySavings = "{0:C2}" -f ($YearlySavings / 12)
         $DisplayYearlyRetirement = "{0:C2}" -f ($YearlyRetirement / 12)
         $DisplayYearlyBrokerage = "{0:C2}" -f ($YearlyBrokerage / 12)
         $DisplayYearlyCrypto = "{0:C2}" -f ($YearlyCrypto / 12)

         Write-Output (
            "Saving: $DisplayYearlySavings into Savings, " +
            "$DisplayYearlyRetirement into Retirement, " +
            "$DisplayYearlyBrokerage into Brokerage, " +
            "and $DisplayYearlyCrypto into Crypto, each month would net you..."
         )

         #############################################

         $Table = @()

         # create first row
         $Row = [PSCustomObject]@{
            Date       = $CurrentYear
            Savings    = $DollarSavings
            Retirement = $DollarRetirement
            Brokerage  = $DollarBrokerage
            Crypto     = $DollarCrypto
            Total      = $DollarTotal
            Notes      = ""
         } 
         $Table += $Row

         # Add subsequent rows
         foreach ($r in 2022..2049)
         {
            $CurrentYear = $r
            $CurrentSavings = $CurrentSavings + $YearlySavings
            $CurrentRetirement = (($CurrentRetirement + $YearlyRetirement) * $RetirementInterest) + $CurrentRetirement + $YearlyRetirement
            $CurrentCrypto = (($CurrentCrypto + $YearlyCrypto) * $CryptoInterest) + $CurrentCrypto + $YearlyCrypto
            $CurrentBrokerage = (($CurrentBrokerage + $YearlyBrokerage) * $BrokerageInterest) + $CurrentBrokerage + $YearlyBrokerage
            $CurrentTotal = $CurrentSavings + $CurrentRetirement + $CurrentBrokerage + $CurrentCrypto

            $DollarSavings = "{0:C2}" -f $CurrentSavings
            $DollarRetirement = "{0:C2}" -f $CurrentRetirement
            $DollarBrokerage = "{0:C2}" -f $CurrentBrokerage
            $DollarCrypto = "{0:C2}" -f $CurrentCrypto
            $DollarTotal = "{0:C2}" -f $CurrentTotal

            $Notes = ""

            if ($CurrentSavings -ge $SavingsTarget)
            {
               $Notes = "Savings requirement met"
            }
            if ($CurrentTotal -ge $Millionair)
            {
               if ($Notes)
               {
                  $Notes = $Notes + "; Over one million saved!"
               }
               else
               {
                  $Notes = "Over one million saved!"
               }
            }

            $Row = [PSCustomObject]@{
               Date       = $CurrentYear
               Savings    = $DollarSavings
               Retirement = $DollarRetirement
               Brokerage  = $DollarBrokerage
               Crypto     = $DollarCrypto
               Total      = $DollarTotal
               Notes      = $Notes
            } 
   
            $Table += $Row
         }
         
         $Table | Format-Table -AutoSize
      }
      Catch
      {
         Write-Error $($_.Exception.Message)
      }
   }

   End
   {
      Stop-Log
   }

}

Get-FutureFinanceProjection

<#######</Body>#######>
<#######</Script>#######>
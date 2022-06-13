import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import { Grid, Container, Typography } from '@mui/material';
import { BrowserRouter, Routes, Route, Switch } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import { faker } from '@faker-js/faker';
import SupplyChain from '../artifacts/contracts/Supplychain.sol/Supplychain.json';
import {
  AppTasks,
  AppNewsUpdate,
  AppOrderTimeline,
  AppCurrentVisits,
  AppWebsiteVisits,
  AppTrafficBySite,
  AppWidgetSummary,
  AppCurrentSubject,
  AppConversionRates,
} from '../sections/@dashboard/app';
import "./index.css";







const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    [`&.${tableCellClasses.body}`]: {
        fontSize: 14,
    },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));

const Home = () => {
    const [unitsList, setUnit] = useState();
    const ContractAddress = '0xb8f91d0C5cc906855f56E91232c655bE06c2dD4a'; 

    async function requestAccount() {
      await window.ethereum.request({ method: 'eth_requestAccounts' });

    }


    useEffect(() => {
      // Update the document title using the browser API
      if(!unitsList){historyAll();}
      console.log(unitsList);
    },[]);

    async function historyAll() {
      if (typeof window.ethereum !== 'undefined') {
        requestAccount();
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        console.log(await signer.getAddress());

        const contract = new ethers.Contract(ContractAddress, SupplyChain.abi, provider);
        try {
          const Pdata = await contract.historyAll();
          console.log('data: ', Pdata);
          setUnit(Pdata);
          } catch (err) {
          console.log('Error: ', err);
        }
      }
    }
    if (unitsList == null) {
      historyAll();
      return (
        <div style={{ textAlign: 'center', padding: '10%' }}>
          <Box sx={{ color: 'grey.500' }}>
            <CircularProgress color="inherit" />
          </Box>
        </div>
      );
    }
    return (
      <>
        <Container>
          <h1 className="heading">UNITS HISTORY</h1>
          <TableContainer component={Paper} sx={{ width: '80%', margin: 'auto', marginTop: '5%' }}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <StyledTableRow>
                  <StyledTableCell>Id</StyledTableCell>
                  <StyledTableCell>GLN</StyledTableCell>
                  <StyledTableCell>SN</StyledTableCell>
                  <StyledTableCell>GSIN</StyledTableCell>
                  <StyledTableCell>GTIN&nbsp;</StyledTableCell>
                  <StyledTableCell>SSCC</StyledTableCell>
                  <StyledTableCell align="left">Data</StyledTableCell>
                  <StyledTableCell align="left">timestamp</StyledTableCell>
                </StyledTableRow>
              </TableHead>
              <TableBody>
                {unitsList.map((row, iterator) => (
                  <StyledTableRow key={iterator} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                    <StyledTableCell component="th" scope="row">
                      {row.id.toNumber()}
                    </StyledTableCell>
                    <StyledTableCell>{row.GLN}</StyledTableCell>
                    {/* <StyledTableCell>{parseInt(row.id._hex)}</StyledTableCell> */}
                    <StyledTableCell>{row.SN}</StyledTableCell>
                    <StyledTableCell>{row.GSIN}</StyledTableCell>
                    <StyledTableCell>{row.GTIN}</StyledTableCell>
                    <StyledTableCell>{row.SSCC}</StyledTableCell>
                    <StyledTableCell>{row[6]}</StyledTableCell>
                    <StyledTableCell>{row.timestamp.toNumber()}</StyledTableCell>
                  </StyledTableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>

          <AppOrderTimeline
            component={Paper}
            sx={{ width: '40%', margin: 'auto', marginTop: '5%' }}
            title="Orders Timeline"
            list={unitsList.map((row, index) => ({
              sn: row.sn,
              title: row.GLN,
              type: `order${index + 1}`,
              time: faker.date.past(),
            }))}
          />
        </Container>
      </>
    );
}
 
export default Home;